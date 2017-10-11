import sqlite3

db = sqlite3.connect("contacts.sqlite")

user_name = input("Please enter the name you're querying: ")
#print(user_name)


user_query = "SELECT * FROM contacts WHERE name = ?"
cursor = db.cursor()
cursor.execute(user_query, (user_name,))
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)



cursor.close()

db.close()

# reason we get the results we got is that we never commited the changes we made in contacts2.py
