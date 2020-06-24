import mysql.connector

my_db = mysql.connector.connect(host="localhost", user="root",
                                password="root1234",  database="best_order_DB")
cursor = my_db.cursor(buffered=True)

cursor.execute("show databases")
for row in cursor.fetchall():
    print(row)

# # # set lists table
# cursor.execute("CREATE TABLE lists (id INTEGER(20), name VARCHAR(255), description VARCHAR(255))")

# # # set lists tasks
# cursor.execute("CREATE TABLE tasks (id INTEGER(20), list_id INTEGER(20), name VARCHAR(255),
# description VARCHAR(255), status VARCHAR(255), priority INTEGER(20), assignee  VARCHAR(255))")

# # # set workers table
# cursor.execute("CREATE TABLE workers (id INTEGER(20), name VARCHAR(50), title VARCHAR(50))")



