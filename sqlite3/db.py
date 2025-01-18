import sqlite3
import os

db_path = r"D:\Python\attendance_tracker.py\students.db"   ## making it a raw string, no escape sequences

# print(os.path.dirname(db_path))

os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)

print("SQlite databaase created successfully")