import sqlite3
from config import DB_NAME

def create_connection():
    """Create and return a database connection"""
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error:{e}")
        return None
    
def create_users_table():
    """Create users table if it does not exist"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                           CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)""")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table:{e}")
        finally:
            conn.close()



def create_transactions_table():
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS transactions(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    type TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    description TEXT,
                    date TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating transactions table: {e}")
        finally:
            conn.close()

def create_budgets_table():
    """Create budgets table"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS budgets(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    month TEXT NOT NULL,
                    year TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            """)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating budgets table: {e}")
        finally:
            conn.close()
