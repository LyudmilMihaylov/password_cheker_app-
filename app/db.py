import sqlite3
from datetime import datetime

DB_NAME = 'passwords.db'

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS password_checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT NOT NULL,
            score INTEGER NOT NULL,
            feedback TEXT NOT NULL,
            checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_password_result(password, score, feedback):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO password_checks (password, score, feedback)
        VALUES (?, ?, ?)
    ''', (password, score, feedback))
    conn.commit()
    conn.close()

def get_all_checks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM password_checks')
    results = cursor.fetchall()
    conn.close()
    return results
