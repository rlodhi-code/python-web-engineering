import sys
from expense_service import (
    fetch_expenses,
    calculate_summary,
    get_today_total,
    get_month_total,
    get_top_category,
    get_daily_totals,
    plot_category_expenses,
    plot_pie_chart,
    save_chart,
    add_expense
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python expense_cli.py [summary|today|month|daily|chart|pie|save]")
        return

    command = sys.argv[1]
    expenses = fetch_expenses()

    if command == "summary":
        total, categories = calculate_summary(expenses)

        print("\n=== SUMMARY ===")
        print(f"Total spent: ${total:.2f}")

        print(f"Current month total: ${get_month_total(expenses):.2f}")

        top = get_top_category(categories)
        print(f"\nTop spending category: {top} (${categories[top]:.2f})")

        print("\n=== BY CATEGORY ===")
        for cat, amt in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"{cat}: ${amt:.2f}")

    elif command == "today":
        print(f"Today's spending: ${get_today_total(expenses):.2f}")

    elif command == "month":
        print(f"Current month spending: ${get_month_total(expenses):.2f}")

    elif command == "daily":
        daily = get_daily_totals(expenses)

        print("\n=== DAILY TOTALS ===")
        for d, amt in sorted(daily.items()):
            print(f"{d}: ${amt:.2f}")

    elif command == "chart":
        _, categories = calculate_summary(expenses)
        plot_category_expenses(categories)

    elif command == "pie":
        _, categories = calculate_summary(expenses)
        plot_pie_chart(categories)

    elif command == "save":
        _, categories = calculate_summary(expenses)
        save_chart(categories)

    elif command == "add":
        if len(sys.argv) < 5:
            print('Usage: python expense_cli.py add "description" amount category')
            return

        description = sys.argv[2]
        amount = sys.argv[3]
        category = sys.argv[4]

        add_expense(description, amount, category)

    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
