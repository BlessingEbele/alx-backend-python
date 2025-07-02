#!/usr/bin/python3
"""
Stream user data row by row from ALX_prodev.user_data using a generator
"""

import mysql.connector


def stream_users():
    """
    Generator function that yields one row at a time from the user_data table
    as a dictionary.
    """
    try:
        connection = mysql.connector.connect(
            user='root',
            password='your_mysql_password_here',  # 🔁 Replace with your actual password
            host='localhost',
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return
