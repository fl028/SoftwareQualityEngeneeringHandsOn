class employee():
  id = None
  surname = None
  lastname = None
  salary = None
  department = None

  def __init__(self,id = None, surname = None, lastname = None, salary = None, department = None):
    self.id = id
    self.surname = surname
    self.lastname = lastname
    self.salary = salary
    self.department = department

  def __str__(self):
    return  self.surname + " " + self.lastname

  def get_new_salary(self):
    return self.salary + 1000
