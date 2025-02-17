import sqlite3  # Importing the sqlite3 module to interact with SQLite databases

# Establishing a connection to the database (if it doesn't exist, it will be created)
conn = sqlite3.connect('students.db')

# Creating a cursor object to interact with the database
cursor = conn.cursor()

# Creating a table 'python_programming' if it doesn't exist, with columns 'id', 'name', and 'grade'
cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER PRIMARY KEY,  # Unique identifier for each student
    name TEXT NOT NULL,      # Name of the student (cannot be null)
    grade INTEGER NOT NULL   # Grade of the student (cannot be null)
)
''')

# Sample data of students to be inserted into the table
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

# Inserting multiple student records into the python_programming table
cursor.executemany('''
INSERT INTO python_programming (id, name, grade)
VALUES (?, ?, ?)  # Placeholders for inserting data into the table
''', students)

# Querying the records where the grade is between 60 and 80 (inclusive)
cursor.execute('''
SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80
''')
# Printing the retrieved records
print("Records with grade between 60 and 80:")
for row in cursor.fetchall():
    print(row)

# Updating the grade of the student with id 55 to 65
cursor.execute('''
UPDATE python_programming SET grade = 65 WHERE id = 55
''')

# Deleting the student record with id 66
cursor.execute('''
DELETE FROM python_programming WHERE id = 66
''')

# Updating the grade of all students with id greater than 55 to 80
cursor.execute('''
UPDATE python_programming SET grade = 80 WHERE id > 55
''')

# Committing the changes to the database inside a try-except block for error handling
try:
    conn.commit()  # Saving changes to the database
except Exception as e:  # If an error occurs, rollback the transaction and print the error
    conn.rollback()
    print(f"Error occurred: {e}")

# Retrieving and printing all records from the python_programming table after updates
cursor.execute('SELECT * FROM python_programming')
print("\nUpdated python_programming table contents:")
for row in cursor.fetchall():
    print(row)

# Closing the database connection after all operations are complete
conn.close()
