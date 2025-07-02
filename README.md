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
- ✅ Stream SQL rows efficiently, row-by-row, using a single loop
- ✅ Create a reusable database seeding pipeline using CSV
- ✅ Combine Python with SQL for real-world backend data handling

---

## 📁 Files in this Directory

| File Name              | Description |
|------------------------|-------------|
| `0-main.py`            | Test script to validate DB seeding and basic SELECT query |
| `seed.py`              | Seeds the `ALX_prodev` MySQL database with `user_data.csv` |
| `user_data.csv`        | Sample dataset used to populate `user_data` table |
| `1-main.py`            | Script to test generator-based row streaming |
| `0-stream_users.py`    | Contains the generator `stream_users()` to stream one row at a time |
| `README.md`            | This file |

---

## ✅ Task 0: Database Seeding Script

**Goal**: Set up the database, table, and populate it with user data from a CSV file.

**Main Script**: `seed.py`

### Key Functions:
```python
def connect_db()
def create_database(connection)
def connect_to_prodev()
def create_table(connection)
def insert_data(connection, csv_file)
`````

✍️ Author
Blessing Ebele Anochili
Backend Developer | Python Enthusiast | ALX SE Program
🔗 GitHub: https://github.com/BlessingEbele/
🌍 Lagos, Nigeria

🔖 License
This project is part of the ALX Software Engineering program and follows the ALX project submission guidelines.
