✅ README.md for python-decorators-0x01 – Task 0

# Python Decorators – Advanced Database Operations

This project demonstrates the use of **Python decorators** to enhance and streamline common database operations. The goal is to reduce boilerplate, add robustness, and improve efficiency and observability in database-driven Python applications.

---

## 📌 Task 0: Logging Database Queries

### Objective:
Create a decorator `log_queries` that logs all SQL queries executed by a decorated function, with a timestamp.

### Key Features:
- Logs SQL query with the current date and time using `datetime`.
- Keeps the original function behavior intact using `functools.wraps`.

### 🧠 Concepts Used:
- Python decorators
- `functools.wraps`
- `datetime.now().strftime()` for timestamp formatting
- SQLite3 database connection and query execution

### ✅ Sample Code:
```python
from datetime import datetime
import functools
import sqlite3

def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get('query') or (args[0] if args else None)
        if query:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"[{now}] Executing SQL Query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
✅ Sample Output:

[2025-06-30 15:24:10] Executing SQL Query: SELECT * FROM users
[('001', 'Blessing Anochili', 'blessing@example.com', 30), ...]
🔁 Directory Structure

python-decorators-0x01/
├── 0-log_queries.py
├── README.md
└── users.db  (optional for testing)
