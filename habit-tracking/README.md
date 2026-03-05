# **📊 Habit Tracking**

A lightweight Python project that uses the Pixela API to record daily habits and visualize progress in a GitHub‑style activity graph. It demonstrates practical API interaction, secure credential management, and clean scripting patterns. Although the example tracks cycling distance, the workflow can be adapted to any habit such as reading, exercise, or coding.

---

## **🧭 Overview**

This project highlights several foundational skills:

- Working with REST APIs in Python  
- Managing secrets using a `.env` file  
- Organizing small automation scripts  
- Performing **POST**, **PUT**, and **DELETE** operations  
- Automating daily habit logging  

Pixela generates a visual graph that updates automatically as entries are added or removed.

---

## **📁 Project Structure**

```
habit-tracking
│
├── setup_pixela.py
├── add_pixel.py
├── delete_pixel.py
├── .env
├── requirements.txt
└── README.md
```

### **File Descriptions**

| File | Purpose |
|------|---------|
| `setup_pixela.py` | Creates the Pixela user, generates a secure token, and initializes the graph |
| `add_pixel.py` | Adds a daily habit entry (“pixel”) to the graph |
| `delete_pixel.py` | Removes an existing pixel from the graph |
| `.env` | Stores credentials and configuration variables |
| `requirements.txt` | Lists required Python packages |

---

## **⚙️ Installation**

### **1. Clone the Repository**

```
git clone https://github.com/yourusername/habit-tracking.git
cd habit-tracking
```

### **2. Install Dependencies**

```
pip install -r requirements.txt
```

Dependencies include:

- `requests`  
- `python-dotenv`

---

## **🚀 Step 1 — Create Pixela Account and Graph**

Run:

```
python setup_pixela.py
```

This script will:

1. Generate a secure API token  
2. Create a Pixela user  
3. Create a habit‑tracking graph  
4. Print the environment variables you must save  

Example output:

```
SAVE THESE VALUES IN YOUR .env FILE

PIXELA_USERNAME=yourusername
PIXELA_TOKEN=yourgeneratedtoken
PIXELA_GRAPH_ID=cycling1
```

---

## **🔐 Step 2 — Create the `.env` File**

Create a file named:

```
.env
```

Add the values printed by the setup script:

```
PIXELA_USERNAME=yourusername
PIXELA_TOKEN=yourgeneratedtoken
PIXELA_GRAPH_ID=cycling1
```

The `.env` file keeps credentials separate from source code and should not be committed to Git.

---

## **📝 Step 3 — Record a Habit Entry**

Run:

```
python add_pixel.py
```

The script will prompt:

```
How many kilometers did you cycle today?
```

After submitting a value, the entry is added to your Pixela graph.

---

## **🗑️ Step 4 — Delete a Habit Entry**

Run:

```
python delete_pixel.py
```

The script will ask:

```
Enter the date to delete (YYYYMMDD)
```

Press **Enter** to delete today’s entry.

---

## **📈 Viewing Your Graph**

Your activity graph is available at:

```
https://pixe.la/@<yourusername>
```

Example:

```
https://pixe.la/@yourusername
```

Pixela automatically visualizes your habit streaks and progress.

---

## **📦 requirements.txt**

```
requests>=2.31.0
python-dotenv>=1.0.0
```

---

## **🔒 Security Notes**

- Never commit `.env` to GitHub.  
- Add `.env` to your `.gitignore`:

```
.env
```

---

## **✨ Possible Improvements**

- Multiple habits and graphs  
- Automatic date handling  
- Command‑line arguments for update/delete operations  
- Error handling for API responses  
- A reusable Pixela client module  
- A visualization dashboard  

---

## **🎯 Learning Goals**

- Python API requests  
- Environment variable management  
- RESTful API interaction  
- Basic project structure  
- Habit‑tracking automation  

---

## **📜 License**

This project is intended for educational use and experimentation. You may modify or extend it for personal or learning purposes.

---
