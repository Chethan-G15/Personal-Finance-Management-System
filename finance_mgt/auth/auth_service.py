from getpass import getpass
import sqlite3
from database.db import create_connection

def register_user():
    """Register a new user with unique username"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()

            ussername = input("enter username:").strip()
            password = getpass("enter password: ")

            cursor.execute(
                "INSERT INTO users (username,password) VALUES(?,?)",
                (ussername,password)
            )
            conn.commit()
            print("Registration Successfull")

        except sqlite3.IntegrityError:
            print("Username already exista.Please try another")
        
        except sqlite3.Error as e:
            print(f"Database error:{e}")
        finally:
            conn.close()

def login_user():
    """Authenticate user login"""
    conn = create_connection()
    if conn:
        try:
            cursor = conn.cursor()

            username = input("Enter username").strip()
            password = getpass("enter password")
            cursor.execute(
                "SELECT * FROM users where username =? AND password =?",
                (username,password)
            )
            user=cursor.fetchone()
            if user:
                print("Login Successful")
                return user[0]
            else:
                print("Invalid username or password")
                return None
        except sqlite3.Error as e:
            print(f"Database error:{e}")
        
        finally:
            conn.close()