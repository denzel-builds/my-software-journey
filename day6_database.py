import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("my_bank.db")

# Create a cursor object to execute SQL commands(This is like my "worker")
cursor = conn.cursor()
# Creating a table, sort of like an excel sheet called users.
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    balance REAL)""")

#Inserting data into the table
cursor.execute("INSERT INTO users (name, age, balance ) VALUES (?, ?, ?)", ("Denzel", 30, 1050.0))
cursor.execute("INSERT INTO users (name, age,balance) VALUES (?,?,?)", ("Thabo", 25, 1500.0))

conn.commit()  # Save (commit) the changes

# Querying or reading data from the table
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

print("All Users in the database:")
for user in all_users:
    print(user)

# Close the connection, always do this at the end
conn.close()
