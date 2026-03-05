# habit-tracking

A simple Python project that uses the Pixela API to track daily habits and visualize progress in a GitHub-style activity graph.

This project demonstrates how to:

* Work with REST APIs in Python
* Manage secrets using `.env`
* Organize small scripts into a clean project structure
* Perform **POST**, **PUT**, and **DELETE** API operations

The application records daily cycling distance, but it can easily be adapted for any habit (reading, exercise, coding, etc.).

---

# Project Structure

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

| File               | Purpose                                                                  |
| ------------------ | ------------------------------------------------------------------------ |
| `setup_pixela.py`  | Creates the Pixela user, generates a secure token, and creates the graph |
| `add_pixel.py`     | Adds a daily habit entry (a "pixel") to the graph                        |
| `delete_pixel.py`  | Deletes an existing pixel from the graph                                 |
| `.env`             | Stores credentials and configuration variables                           |
| `requirements.txt` | Lists required Python packages                                           |

---

# Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/habit-tracking.git
cd habit-tracking
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

Dependencies:

* requests
* python-dotenv

---

# Step 1 — Create Pixela Account and Graph

Run the setup script:

```
python setup_pixela.py
```

This script will:

1. Generate a secure API token
2. Create a Pixela user
3. Create a habit tracking graph
4. Print environment variables you must save

Example output:

```
SAVE THESE VALUES IN YOUR .env FILE

PIXELA_USERNAME=yourusername
PIXELA_TOKEN=yourgeneratedtoken
PIXELA_GRAPH_ID=cycling1
```

---

# Step 2 — Create the `.env` File

Create a file named:

```
.env
```

Add the variables printed by the setup script.

Example:

```
PIXELA_USERNAME=yourusername
PIXELA_TOKEN=yourgeneratedtoken
PIXELA_GRAPH_ID=cycling1
```

The `.env` file keeps credentials separate from source code.

---

# Step 3 — Record a Habit Entry

Run:

```
python add_pixel.py
```

The script will ask:

```
How many kilometers did you cycle today?
```

After submission, the value is recorded on the Pixela graph.

---

# Step 4 — Delete a Habit Entry

Run:

```
python delete_pixel.py
```

The script will ask for a date:

```
Enter the date to delete (YYYYMMDD)
```

Press **Enter** to delete today's entry.

---

# Example Graph

Your graph will be available at:

```
https://pixe.la/@<yourusername>
```

Example:

```
https://pixe.la/@yourusername
```

Pixela automatically visualizes your habit activity.

---

# requirements.txt

```
requests>=2.31.0
python-dotenv>=1.0.0
```

---

# Security Notes

* Never commit `.env` to GitHub.
* Add `.env` to your `.gitignore`.

Example `.gitignore` entry:

```
.env
```

---

# Possible Improvements

Future enhancements could include:

* Multiple habits and graphs
* Automatic date handling
* Command-line arguments for update/delete operations
* Error handling for API responses
* A reusable Pixela client module
* Visualization dashboard

---

# Learning Goals

This project is useful for learning:

* Python API requests
* Environment variable management
* RESTful API design
* Basic project structure
* Habit tracking automation

---

# License

This project is intended for educational use and experimentation.
