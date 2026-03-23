# 🏋️ Workout Logger  
A simple Python script that takes natural‑language exercise input (e.g., *“I ran 3 miles and did 20 minutes of yoga”*), sends it to the **Nutritionix Exercise API**, and logs the parsed workout data into a **Google Sheet** using **Sheety.co**.

This project is ideal for learning API integration, environment variable management, and lightweight data logging workflows.

---

## 📌 Important Note About Nutritionix  
As of 2024–2025, **Nutritionix has discontinued free personal accounts**.  
This means new users **cannot** obtain an APP ID and API Key without a paid plan.

Because of this, the Nutritionix portion of the script can be **skipped or commented out** if you only want to test the Sheety integration.  
Sheety **still offers free accounts**, so the logging portion works without issue.

---

## 🚀 Features  
- Accepts natural-language exercise descriptions  
- Sends exercise text to Nutritionix (if credentials available)  
- Extracts calories, duration, and exercise names  
- Logs each exercise entry into a Google Sheet via Sheety  
- Uses environment variables for secure credential handling  

---

## 📂 Project Structure  
```
workout_logger.py
.env
README.md
```

---

## 🔧 Requirements  
- Python 3.8+  
- `requests`  
- `python-dotenv`  

Install dependencies:

```bash
pip install requests python-dotenv
```

---

## ⚙️ Environment Variables  
Your `.env` file should contain:

```
APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
ENDPOINT=https://api.sheety.co/<your-project>/workouts/workouts
USERNAME=your_sheety_username
PASSWORD=your_sheety_password
TOKEN=your_sheety_token_if_used
```

> **Reminder:** Nutritionix free accounts are no longer available.  
> If you don’t have APP_ID and API_KEY, comment out the Nutritionix section and manually create test data.

---

## ▶️ How to Run  
```bash
python workout_logger.py
```

You will be prompted:

```
Tell me which exercises you did:
```

Example input:

```
I cycled for 30 minutes and did 15 minutes of weight lifting
```

If Nutritionix credentials are valid, the script will parse the exercises and send them to your Sheety-powered Google Sheet.

---

## 📝 How the Script Works  
### 1. Load environment variables  
Uses `dotenv` to keep credentials out of the code.

### 2. Send exercise text to Nutritionix  
Nutritionix returns structured data such as:
- exercise name  
- duration  
- calories burned  

### 3. Format the data  
Adds date and time using `datetime.now()`.

### 4. Send each exercise entry to Sheety  
Sheety converts a simple REST POST request into a new row in your Google Sheet.

---

## 🧾 Why Use Sheety Instead of Google APIs Directly?  
Using Google Sheets API directly is powerful but comes with significant overhead.  
Sheety simplifies this dramatically.

### ⭐ Benefits of Using Sheety  
- **No OAuth complexity** — Google APIs require OAuth 2.0, token refresh, scopes, and credential files. Sheety uses simple Basic Auth or Bearer tokens.  
- **Instant REST API** — Sheety turns any Google Sheet into a REST endpoint automatically.  
- **Beginner-friendly** — Perfect for small automation scripts, prototypes, and personal projects.  
- **No Google Cloud setup** — Avoids enabling APIs, creating service accounts, downloading JSON credentials, and managing permissions.  
- **Consistent JSON interface** — Easy to integrate with Python, JavaScript, or no-code tools.  
- **Free tier available** — Unlike Nutritionix, Sheety still offers free usage for personal projects.  

### When Google APIs *might* be better  
- Large-scale automation  
- High-volume writes  
- Complex Sheets operations (batch updates, formatting, formulas)  
- Enterprise workflows requiring strict IAM controls  

For most personal fitness logging projects, **Sheety is faster, simpler, and easier to maintain**.

---

## 🛠️ Customization Ideas  
- Add step tracking or heart rate data  
- Log workouts to Notion or Airtable instead of Google Sheets  
- Add a GUI or Telegram/Discord bot interface  
- Schedule daily reminders to log workouts  

---

