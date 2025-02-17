import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL
)
''')

students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

cursor.executemany('''
INSERT INTO python_programming (id, name, grade)
VALUES (?, ?, ?)
''', students)

cursor.execute('''
SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80
''')
print("Records with grade between 60 and 80:")
for row in cursor.fetchall():
    print(row)

cursor.execute('''
UPDATE python_programming SET grade = 65 WHERE id = 55
''')

cursor.execute('''
DELETE FROM python_programming WHERE id = 66
''')

cursor.execute('''
UPDATE python_programming SET grade = 80 WHERE id > 55
''')

try:
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Error occurred: {e}")

cursor.execute('SELECT * FROM python_programming')
print("\nUpdated python_programming table contents:")
for row in cursor.fetchall():
    print(row)

conn.close()
