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


🧩 Task 1: Handle Database Connections with a Decorator
🎯 Objective:
Implement a decorator with_db_connection that automatically manages opening and closing of a SQLite database connection.

💡 Key Features:
Removes boilerplate connection handling.

Injects the connection (conn) into the decorated function.

Ensures proper cleanup using try...finally.

🧠 Concepts Used:
Python decorators

functools.wraps

Resource management with try...finally

SQLite connection injection

✅ Sample Code:
python
import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
✅ Sample Output:
bash

('001', 'Blessing Anochili', 'blessing@example.com', 30)

🧾 Task 2: Transaction Management Decorator
🎯 Objective:
Create a @transactional decorator to wrap database operations inside a transaction. It should:

Commit changes when successful

Rollback if an error occurs

This ensures atomicity and protects data integrity during database updates.

🔧 Decorator Stack:
The function uses two decorators:

@with_db_connection: Handles opening/closing DB connections.

@transactional: Manages commit/rollback logic.

🧠 Concepts Used:
Python decorators

Error handling with try/except

SQLite transaction management

Decorator stacking

✅ Sample Code:
python

def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("[TRANSACTION] Committed successfully.")
            return result
        except Exception as e:
            conn.rollback()
            print(f"[TRANSACTION] Rolled back due to error: {e}")
            raise
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
✅ Sample Output:
pgsql

[TRANSACTION] Committed successfully.
Or, on failure:

pgsql

[TRANSACTION] Rolled back due to error: no such column: email_address

🔁 Directory Structure
📂 Project Structure

python-decorators-0x01/
├── 0-log_queries.py
├── 1-with_db_connection.py
├── 2-transactional.py
├── README.md
└── users.db

