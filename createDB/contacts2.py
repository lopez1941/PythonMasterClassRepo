import sqlite3
db = sqlite3.connect("contacts.sqlite")  # connecting to the db that already exists


update_sql = "UPDATE contacts SET email = 'Update@update.com'"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))
print("Are connections the same: {}".format(update_cursor.connection == db))

update_cursor.connection.commit()

update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)


db.close()