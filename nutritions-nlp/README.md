# **🔥 Exercise Calories Calculator (Nutrition NLP)**

A Python project that uses the **Nutritionix Natural Language Exercise API** to estimate calories burned from exercises described in plain English. The program accepts free‑form text such as:

```
swam for 1 hour
```

and returns structured exercise data including:

- Exercise name  
- Duration  
- Calories burned  

This project demonstrates practical REST API usage, JSON requests, environment variable management, and lightweight NLP‑powered exercise parsing.

---

## **🧭 Overview**

The project highlights several foundational skills:

- Sending REST API requests  
- Parsing JSON responses  
- Managing API credentials with `.env`  
- Using natural language input to trigger structured exercise analysis  
- Structuring small Python automation scripts  

---

## **💡 Example**

**Input:**

```
Tell me which exercises you did: swam for 1 hour
```

**Example Output:**

```
Exercise: swimming
Duration: 60 minutes
Calories burned: 919
```

---

## **📁 Project Structure**

```
nutrition-calorie-tracker
│
├── calculate_calories.py
├── .env
├── requirements.txt
└── README.md
```

### **File Descriptions**

| File | Purpose |
|------|---------|
| `calculate_calories.py` | Main script that sends exercise text to the API |
| `.env` | Stores API credentials and user profile data |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

---

## **⚙️ Requirements**

- Python 3.8+  
- Internet connection  
- Nutritionix API credentials  

You may run the project using a terminal, VS Code, PyCharm, or any Python IDE.

---

## **📦 Installation**

### **1. Clone the repository**

```
git clone https://github.com/yourusername/nutrition-calorie-tracker.git
cd nutrition-calorie-tracker
```

### **2. Install dependencies**

```
pip install -r requirements.txt
```

---

## **🔐 Environment Variables**

Create a `.env` file in the project root directory.

**Example:**

```
GENDER=male
WEIGHT=75
HEIGHT=175
AGE=40

APP_ID=your_app_id
API_KEY=your_api_key
```

### **Variable Description**

| Variable | Description |
|----------|-------------|
| `GENDER` | male or female |
| `WEIGHT` | weight in kilograms |
| `HEIGHT` | height in centimeters |
| `AGE` | age in years |
| `APP_ID` | Nutritionix application ID |
| `API_KEY` | Nutritionix API key |

---

## **🏃 Running the Program**

Run the script:

```
python calculate_calories.py
```

The program will prompt:

```
Tell me which exercises you did:
```

Enter a natural language description of your workout.

**Examples:**

```
ran 3 miles
swam for 1 hour
walked for 30 minutes and did 20 minutes of yoga
```

The API will return structured exercise information including calories burned.

---

## **📚 Dependencies**

```
requests>=2.31.0
python-dotenv>=1.0.0
```

---

## **🔒 Security Note**

Do **not** commit `.env` to GitHub.

Add this to `.gitignore`:

```
.env
```

---

## **✨ Possible Improvements**

- Logging workouts to **Google Sheets**  
- Storing exercise history in a **database**  
- Supporting multiple users  
- Building a **web interface**  
- Generating daily or weekly summaries  

---

## **🎯 Learning Goals**

- Working with external APIs  
- Parsing JSON responses  
- Using environment variables  
- Structuring small Python automation projects  

---

## **📜 License**

This project is intended for educational purposes and experimentation.

---

