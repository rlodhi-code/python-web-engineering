import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import matplotlib.pyplot as plt

load_dotenv()

ENDPOINT = os.getenv("SHEETY_ENDPOINT")
USERNAME = os.getenv("SHEETY_USERNAME")
PASSWORD = os.getenv("SHEETY_PASSWORD")


def fetch_expenses():
    response = requests.get(ENDPOINT, auth=(USERNAME, PASSWORD))
    data = response.json()
    return data.get("expenses", [])


def calculate_summary(expenses):
    total_spent = 0
    category_totals = {}

    for item in expenses:
        amount = float(item["amount"])
        category = item["category"]

        total_spent += amount
        category_totals[category] = category_totals.get(category, 0) + amount

    return total_spent, category_totals


def get_today_total(expenses):
    today = datetime.now().strftime("%Y-%m-%d")
    return sum(float(e["amount"]) for e in expenses if e["date"] == today)


def get_month_total(expenses):
    current_month = datetime.now().strftime("%Y-%m")
    return sum(float(e["amount"]) for e in expenses if e["date"].startswith(current_month))


def get_top_category(category_totals):
    return max(category_totals, key=category_totals.get)


def get_daily_totals(expenses):
    daily_totals = {}

    for item in expenses:
        date = item["date"]
        amount = float(item["amount"])

        daily_totals[date] = daily_totals.get(date, 0) + amount

    return daily_totals


# 📊 BAR CHART
def plot_category_expenses(category_totals):
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure()
    plt.bar(categories, amounts)
    plt.xticks(rotation=45)
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.tight_layout()
    plt.show()


# 🥧 PIE CHART
def plot_pie_chart(category_totals):
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()


# 💾 SAVE CHART
def save_chart(category_totals):
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.figure()
    plt.bar(categories, amounts)
    plt.xticks(rotation=45)
    plt.title("Expenses by Category")
    plt.tight_layout()
    plt.savefig("expenses.png")
    print("Chart saved as expenses.png\n")

# following code supports adding more entries/data to Google Sheet expenses
# usage is python expense_cli.py add "coffee" 5 Food
def add_expense(description, amount, category):
    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")

    payload = {
        "expense": {
            "date": today,
            "category": category,
            "description": description,
            "amount": float(amount)
        }
    }

    response = requests.post(
        ENDPOINT,
        json=payload,
        auth=(USERNAME, PASSWORD)
    )

    if response.status_code == 200 or response.status_code == 201:
        print("Expense added successfully!")
        print(response.json())
    else:
        print("Failed to add expense")
        print(response.text)