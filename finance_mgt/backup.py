import shutil
from config import DB_NAME

def backup_database():
    try:
        shutil.copy(DB_NAME, "finance_backup.db")
        print("Backup created successfully!")
    except Exception as e:
        print("Backup failed:", e)


def restore_database():
    try:
        shutil.copy("finance_backup.db", DB_NAME)
        print("Database restored successfully!")
    except Exception as e:
        print("Restore failed:", e)