import sqlite3
try:
    from model_employee import employee
except:
    from .model_employee import employee


class DB():
    connection = None
    employee_peter = employee(None,"Peter","Maier",100000,"Development")
    employee_juergen = employee(None,"Juergen","Dieter",25000,"IT")
    employee_max = employee(None,"Max","Mustermann",30000,"Marketing")
    initial_employees = [employee_peter,employee_juergen,employee_max]

    def __init__(self):
        self.connection = sqlite3.connect("employees.db")

    def __del__(self):
        self.connection.close()

    def init_db(self):
        cursor = self.connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS employees")

        cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT, lastname TEXT, salary INTEGER, department TEXT)")
        for i in range(len(self.initial_employees)):
            cursor.execute("INSERT INTO employees (surname,lastname,salary,department) values (?,?,?,?)",[self.initial_employees[i].surname,self.initial_employees[i].lastname,self.initial_employees[i].salary,self.initial_employees[i].department])

        self.connection.commit()

    def get_all_employees(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from employees")
        employees = cursor.fetchall()
        return employees

if __name__ == '__main__':
    db = DB()
    db.init_db()