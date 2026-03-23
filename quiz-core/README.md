# 🎯 Quiz Application (Python + Open Trivia DB API)

This project is a lightweight, modular Python application that generates interactive quiz questions by pulling data from the **Open Trivia Database API**. The design emphasizes clarity, separation of concerns, and easy customization, making it simple to extend or adapt for different quiz formats.

---

## 📌 Overview

The application retrieves trivia questions from:

**https://opentdb.com/api.php?amount=5&type=boolean**

It then builds a quiz experience using a small collection of Python modules that handle:

- Fetching and preparing data  
- Structuring questions  
- Managing quiz logic  
- Displaying the user interface  

The result is a clean, event‑driven quiz program that can be easily modified or expanded.

---

## 🌐 How the Data Is Retrieved

A dedicated module handles all API communication.  
It sends a request to the Open Trivia DB endpoint with configurable parameters such as:

- Number of questions  
- Question type (e.g., boolean, multiple choice)  
- Difficulty level  
- Category  

The returned JSON is parsed and converted into a list of question objects used by the quiz engine.

---

## 🧠 Core Components

### **1. Data Module**
Responsible for calling the API and returning structured question data.  
Parameters can be tweaked to change the quiz content without modifying the rest of the application.

### **2. Question Model**
Defines a simple object representing each question and its correct answer.

### **3. Quiz Engine (QuizBrain)**
Handles the quiz flow, including:

- Tracking the current question  
- Checking answers  
- Updating the score  
- Determining when the quiz ends  

It also safely decodes HTML‑encoded text returned by the API. 
**https://www.freeformatter.com/html-escape.html)**

### **4. User Interface**
A separate UI module (e.g., Tkinter) presents questions, captures user input, and displays feedback.

---

## 🧩 Application Flow

1. Fetch question data from the API  
2. Convert each item into a `Question` object  
3. Build a question bank  
4. Pass the bank into the quiz engine  
5. Launch the UI and begin the quiz  
6. Continue until all questions are answered  

---

## 🔧 Customization

The application is intentionally flexible.  
You can easily adjust:

- Number of questions  
- Question type (boolean, multiple choice)  
- Categories  
- Difficulty  
- UI behavior  
- Scoring rules  

All changes can be made by modifying the parameters in the data module or extending the quiz engine.

---

## 📦 Project Purpose

This project serves as a clean example of:

- Working with external APIs  
- Structuring Python applications into logical modules  
- Building interactive programs  
- Separating data, logic, and presentation layers  

It’s an excellent foundation for experimenting with more advanced quiz features or integrating additional APIs.

---
