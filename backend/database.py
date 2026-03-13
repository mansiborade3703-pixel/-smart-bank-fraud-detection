
# Database connection placeholder

import sqlite3

def get_connection():
    conn = sqlite3.connect('bank.db')
    return conn
