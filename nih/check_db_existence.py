import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_file_path = os.path.join(BASE_DIR, 'db.sqlite3')

if os.path.exists(db_file_path):
    print("File database ditemukan di:", db_file_path)
else:
    print("File database tidak ditemukan di:", db_file_path)
