import sqlite3
import sys

def run_database_operations():
    conn = None
    try:
        conn = sqlite3.connect('example.db')
        print("Connected to the database successfully")
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        print('Table "users" created or already exists.')

        user_to_insert = [
            ('Alice', 'alice@example.com'),
            ('Bob', 'bob@example.com'),
            ('Charlie', 'charlie@example.com'),
        ]

        try:
            cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", user_to_insert)
            print("Inserted new records into the table (if they didn't already exist).")
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Insertion skipped: {e}. Records with these emails already exist.")

        print("\n---Reading all records---")
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

        print("\n---Updating Records---")
        cursor.execute("UPDATE users SET email=? WHERE name=?",
                       ('robert@example.com', 'Bob'))
        print("Updated Bob's email.")
        conn.commit()

        print("\n---Deleting a record---")
        cursor.execute("DELETE FROM users WHERE name=?", ('Charlie',))
        conn.commit()
        print("Deleted Charlie.")

        print("\n---Reading records after update and delete---")
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    except sqlite3.IntegrityError as e:
        print(f"\nDatabase Integrity Error: {e}")
    except sqlite3.Error as e:
        print(f"\nAn unexpected SQLite error occurred: {e}")
    except Exception as e:
        print(f"\nAn unexpected system error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    run_database_operations()