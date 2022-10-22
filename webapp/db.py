import sqlite3

employees = [
["Peter","Maier",100000,"Development"],
["Juergen","Dieter",25000,"IT"],
["Max","Mustermann",30000,"Marketing"]
]

employees = sorted(employees)

connection = sqlite3.connect("employees.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS employees")

cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT, lastname TEXT, salery INTEGER, department TEXT)")
for i in range(len(employees)):
    cursor.execute("INSERT INTO employees (surname,lastname,salery,department) values (?,?,?,?)",[employees[i][0],employees[i][1],employees[i][2],employees[i][3]])

connection.commit()
connection.close()