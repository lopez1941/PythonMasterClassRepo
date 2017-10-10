import sqlite3

db = sqlite3.connect("contacts.sqlite")

cursor = db.cursor()
cursor.execute("select * from contacts")
for row in cursor:
    print(row)


cursor.close()

db.close()

# reason we get the results we got is that we never commited the changes we made in contacts2.py