import sqlite3

# will create the database if it doesn't already exist
# if it does exist, it will open the database
db = sqlite3.connect("contacts.sqlite")

# db.execute executes sql commands same as if we were at the command line
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@email.com')")

cursor = db.cursor()
# cursor.execute("SELECT * FROM contacts")
# for row in cursor:
#     print(row)

cursor.execute("SELECT * FROM contacts")
#print(cursor.fetchall())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)



cursor.close()

# make sure you commit any changes to the db, otherwise you'll lose them when the db closes
db.commit()

db.close()
