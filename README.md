# Quiz Scorer

## 📌 Project Overview

Quiz Scorer is a simple Python program that calculates and analyzes quiz scores.  
It is designed to demonstrate basic function design, modular coding, and unit testing using Python.

The program can:

- Calculate total score
- Calculate average score
- Find highest score
- Find lowest score
- Generate a summary of results
- Run unit tests to verify correctness

---

## 📂 Project File's name

```
Quiz.py
```
test_quiz.py
```
README.md
```

---

## 🧠 Functions of (Quiz.py)

### total_score(scores)
Returns the sum of all scores.

### average_score(scores)
Returns the average score.  
If the list is empty, it returns 0.

### highest_score(scores)
Returns the highest score.  
If the list is empty, it returns None.

### lowest_score(scores)
Returns the lowest score.  
If the list is empty, it returns None.

### score_(scores)
Returns a dictionary containing:
- total
- average
- highest
- lowest

---

## ▶ How to Run the Program

Run the main file:

```
python Quiz.py
```

Enter scores separated by spaces.

Example:
```
80 90 70 60
```

---

## 🧪 Unit Testing

This project uses Python’s built-in `unittest` module.

### What is Tested

- Total score calculation
- Average score calculation
- Highest score
- Lowest score
- Summary dictionary correctness

Run tests using:

```
python -m unittest test_quiz.py
```

---

## 🐞 Bugs Found and Fixed

- Function name mismatch (`score_things` → `score_summary`)
- Case sensitivity issue in file name (`Quiz.py`)
- Average calculation handling for empty list
- Ensured correct dictionary keys in summary

Unit testing helped identify and fix these issues.

---

## 🎯 Learning Outcomes

- Writing reusable functions
- Using `if __name__ == "__main__"`
- Implementing unit tests
- Debugging using automated testing
- Organizing a small Python project properly

---

## Made by:
*Md. Arham Ishtiyaque*