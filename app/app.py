import re
from db import create_connection, create_table, insert_password

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[\W_]", password):
        return False
    return True

def main():
    conn = create_connection("passwords.db")
    create_table(conn)

    password = input("Enter a password: ")
    if check_password_strength(password):
        insert_password(conn, password)
        print("Password is strong and saved.")
    else:
        print("Password is weak.")

if __name__ == "__main__":
    main()
