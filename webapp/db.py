from multiprocessing import connection
import sqlite3

class DB():
    connection = None
    initial_employees = [
    ["Peter","Maier",100000,"Development"],
    ["Juergen","Dieter",25000,"IT"],
    ["Max","Mustermann",30000,"Marketing"]
    ]

    def __init__(self):
        self.connection = sqlite3.connect("employees.db")

    def __del__(self):
        self.connection.close()

    def init_db(self):
        employees = sorted(self.initial_employees)

        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS employees")

        cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT, lastname TEXT, salery INTEGER, department TEXT)")
        for i in range(len(employees)):
            cursor.execute("INSERT INTO employees (surname,lastname,salery,department) values (?,?,?,?)",[employees[i][0],employees[i][1],employees[i][2],employees[i][3]])

        self.connection.commit()
        
    def get_all_employees(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from employees")
        employees = cursor.fetchall()
        return employees

if __name__ == '__main__':
    db = DB()
    db.init_db()