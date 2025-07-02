# 🌀 ALX Backend Python – Generators & SQL Streaming

Welcome to the **Python Generators and SQL Integration Module** of the ALX Backend curriculum.  
This project demonstrates how to work with **Python generators**, large datasets, and **real-time SQL streaming** in a memory-efficient way.

---

## 📚 Project Overview

This module focuses on using Python's `yield` and generator functions to process data **efficiently** and **incrementally** — an essential skill for backend developers working with **large datasets**, **streaming applications**, and **live dashboards**.

---

## 📁 Directory Structure

alx-backend-python/
├── python-generators-0x00/
│ ├── 0-main.py
│ ├── seed.py
│ ├── user_data.csv
│ ├── README.md
│ └── ...
├── README.md <-- (this file)


---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

- ✅ Create Python **generator functions** using `yield`
- ✅ Stream data from a **SQL database row-by-row**
- ✅ Handle **large datasets** without overloading memory
- ✅ Simulate **real-world streaming behavior**
- ✅ Use **SQL queries dynamically** inside Python
- ✅ Integrate **Python + MySQL/SQLite** for high-performance data access

---

## 🔧 Technologies & Tools

- **Python 3.x**
- **MySQL** (via `mysql-connector-python`)
- **CSV & file handling**
- **UUIDs, Indexed Primary Keys**
- **SQL Performance Profiling**

---

## 🚀 Getting Started

### Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/alx-backend-python.git
cd alx-backend-python/python-generators-0x00
Install dependencies:


pip install mysql-connector-python
Update seed.py with your actual MySQL password and run:


chmod +x 0-main.py
./0-main.py
🧪 What You’ll Build
✅ A full pipeline that:

Seeds a MySQL database (ALX_prodev)

Creates a user_data table with UUIDs

Populates it from a CSV file

Streams rows one-by-one using a generator function (in the next task)

`````
# 🌀 Python Generators with SQL Integration

This directory contains Python scripts that demonstrate **advanced usage of generator functions** for efficient, memory-safe data processing using **SQL databases**.

It is part of the **ALX Backend Python** project series.

---

## 📚 Learning Objectives

By completing this module, you will:

- ✅ Use Python generator functions with `yield` to iterate through large datasets
- ✅ Stream SQL rows efficiently, row-by-row or in batches
- ✅ Handle large data without memory overload
- ✅ Process batches with filtering logic
- ✅ Seed SQL databases from CSV
- ✅ Combine Python with MySQL for real-world backend use cases

---

## 📁 Files in this Directory

| File Name              | Description |
|------------------------|-------------|
| `0-main.py`            | Script to test DB creation and seeding |
| `seed.py`              | Creates MySQL DB (`ALX_prodev`), `user_data` table, and seeds from CSV |
| `user_data.csv`        | Sample dataset with user information |
| `1-main.py`            | Test script to print rows using generator from `0-stream_users.py` |
| `0-stream_users.py`    | Streams rows one at a time using generator |
| `2-main.py`            | Tests batch streaming & filtering from `1-batch_processing.py` |
| `1-batch_processing.py`| Streams user data in batches & filters for users older than 25 |
| `README.md`            | This file |

---

## ✅ Task 0: Seed MySQL Database

**Goal:** Create `ALX_prodev` DB and populate `user_data` table using `user_data.csv`.

**Script:** `seed.py`

### Functions:
```python
def connect_db()
def create_database(connection)
def connect_to_prodev()
def create_table(connection)
def insert_data(connection, csv_file)
✅ Task 1: Stream SQL Rows One-by-One
Goal: Use a generator to lazily stream individual user rows from the user_data table.

Script: 0-stream_users.py
Tested with: 1-main.py

Function:
python
def stream_users()
✅ Task 2: Batch Processing with Generators
Goal: Use generator to process user records in batches, then filter and print only users over the age of 25.

Script: 1-batch_processing.py
Tested with: 2-main.py

Functions:
python
def stream_users_in_batches(batch_size)
def batch_processing(batch_size)

Sample Output:
bash
{'user_id': '00234e...', 'name': 'Dan Altenwerth Jr.', 'age': 67}
{'user_id': '006bfede...', 'name': 'Glenda Wisozk', 'age': 119}
...
✅ Memory Efficient
✅ Processes data in chunks
✅ Only 3 loops used


`````

✍️ Author
Blessing Ebele Anochili
Backend Developer | Python Enthusiast | ALX SE Program
🔗 GitHub: https://github.com/BlessingEbele/
🌍 Lagos, Nigeria

🔖 License
This project is part of the ALX Software Engineering program and follows the ALX project submission guidelines.
