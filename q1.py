import sqlite3

try:
    # Connect to SQLite database
    connection = sqlite3.connect("students.db")

    # Create a cursor
    cursor = connection.cursor()

    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)

    # Insert data
    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        ("Tatenda", 22)
    )

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        ("John", 25)
    )

    # Save changes
    connection.commit()

    # Retrieve data
    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    # Display retrieved data
    print("Student Records:")
    for row in rows:
        print(row)

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()
        print("Database connection closed.")