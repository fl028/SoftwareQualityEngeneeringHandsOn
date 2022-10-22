import sqlite3
from flask import Flask, render_template, g, jsonify,url_for,redirect, request

app = Flask(__name__)
app.secret_key = "dev"

# db

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('employees.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.commit()
        db.close()

# views

@app.route("/")
def view_index():
    return render_template("index.html")

@app.route("/employees")
def view_employees():
    #call own api
    employees = api_employees()
    count = api_employees_count()
    return render_template("employees.html", data = employees.json['data'], count = count.json['data'])

@app.route('/employees/create')
def view_employees_create():
    return render_template("employeescreate.html")

@app.route('/employees/create', methods=["post"])
def view_employees_create_by_form():
    employee = {
        "surname": request.form['surnameInput'],
        "lastname": request.form['lastnameInput'],
        "salery": request.form['saleryInput'],
        "department": request.form['departmentInput'],
    }
    #call own api
    response = api_employees_create(employee)
    return redirect(url_for("view_employees"))

@app.route('/employees/delete/<id>', methods=["post"])
def view_employees_delete_by_button(id):
    #call own api
    response = api_employees_delete(id)
    return redirect(url_for("view_employees"))

# api

@app.route('/api/employees')
def api_employees():
    cur = get_db().cursor()
    cur.execute("select * from employees")
    employees = cur.fetchall()
    return jsonify(data = employees)

@app.route('/api/employees/create', methods=["post"])
def api_employees_create(employee = None):
    if employee == None:
        employee = request.get_json()
    cur = get_db().cursor()
    cur.execute("INSERT INTO employees (surname,lastname,salery,department) values (?,?,?,?)",[employee["surname"],employee["lastname"],employee["salery"],employee["department"]])
    return ('', 200)

@app.route('/api/employees/delete/<id>', methods=["post"])
def api_employees_delete(id):
    cur = get_db().cursor()
    cur.execute(f"delete from employees where id = {id}")
    return ('', 200)

@app.route('/api/employees/count')
def api_employees_count():
    cur = get_db().cursor()
    cur.execute("select * from employees")
    employees = cur.fetchall()
    return jsonify(data = len(employees))

