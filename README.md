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

✍️ Author
Blessing Ebele Anochili
Backend Developer | Python Enthusiast | ALX SE Program
🔗 GitHub: https://github.com/BlessingEbele/
🌍 Lagos, Nigeria

🔖 License
This project is part of the ALX Software Engineering program and follows the ALX project submission guidelines.
