# Student Performance Prediction System (ML)

A Machine Learning-based console application designed to analyze student data and predict their final marks and grades based on key academic factors like attendance, study hours, assignments, internal marks, and previous performance.

This project was built as part of the **CodeVedX** AI/ML Internship (Project 2: Training + Data Analysis Tool).

---

## 📌 Project Overview
The main objective of this project is to apply Data Preprocessing, Exploratory Data Analysis (EDA), Data Visualization, and Linear Regression to predict student outcomes. It helps in identifying student performance trends and evaluating model accuracy using the R² Score.

### 🎯 Key Features
- **Data Cleaning & Preprocessing:** Handles missing values automatically by replacing them with the column mean.
- **Exploratory Data Analysis (EDA):** Generates dataset summaries, statistical descriptions, and a correlation matrix.
- **Data Visualization:** Plots critical charts like *Study Hours vs Final Marks* (Scatter Plot) and *Attendance Distribution* (Histogram) using Matplotlib.
- **Predictive Modeling:** Uses a Linear Regression model to predict final marks.
- **Grade Generation:** Automatically assigns grades (A+, A, B, C, Fail) based on predicted marks.
- **Interactive Console Input:** Allows users to input real-time student data to predict scores instantly.

---

## 🛠️ Tech Stack & Libraries Used
- **Language:** Python
- **Libraries:**
  - `pandas` (Data loading and manipulation)
  - `matplotlib` (Data visualization)
  - `scikit-learn` (Model training, train-test split, and evaluation)
  - `os` (Automatic file path management)

---

## 📊 Feature Selection
The model utilizes the following independent features ($X$) to predict the target variable ($y$ - Final Marks):
1. **Attendance**
2. **Study Hours**
3. **Assignment Score**
4. **Internal Marks**
5. **Previous Marks**

---

## 🚀 How to Run the Project

### 1. Prerequisites
Make sure you have Python installed on your system. You will also need to install the required libraries:
```bash
pip install pandas matplotlib scikit-learn
```
2. Dataset Setup
Ensure you have a CSV file named student_data.csv placed in the same directory as the script. The script automatically detects the file path using Python's os library.

3. Execution
Run the Python script using your terminal or VS Code:
```bash
python student_predictor.py
```
