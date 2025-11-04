from db_connect import DataConnect

class Employees:
  def __init__(self):
    self.db = DataConnect()

  def view_employees(self):
    query = "SELECT employee_id, last_name, first_name, title, title_of_courtesy FROM employees"
    self.db.cursor.execute(query)

    rows = self.db.cursor.fetchall()

    if not rows:
      print("no employee can be found")
    else:
      print("\n========= EMPLOYEES =========")

      for row in rows:
        employee_id = row[0]
        last_name = row[1]
        first_name = row[2]
        title = row[3]
        title_of_courtesy = row[4]
        print(f"{employee_id}. {title_of_courtesy} {first_name} {last_name}, {title}")
    
    # return rows
    while True:
      user_choice = input("enter the EMPLOYEE ID to view details (or type 'b' to go back): ").strip().lower()

      if user_choice == 'b':
        print("Going back...")
        return
      
      if not user_choice.isdigit():
          print("Invalid input. Please enter a number or 'b' to go back.")
          continue
      
      emp_id = int(user_choice)
      query = """
        SELECT employee_id, last_name, first_name, title, title_of_courtesy,
               birth_date, hire_date, address, city, region, postal_code,
               country, home_phone, extension, photo, notes
        FROM employees
        WHERE employee_id = %s
      """
      self.db.cursor.execute(query, (emp_id,))
      employee = self.db.cursor.fetchone()

      if not employee:
          print(f"No employee found with ID {emp_id}. Try again or type 'b' to go back.")
      else:
          print("\n========= EMPLOYEE DETAILS =========")
          fields = [
              "Employee ID", "Last Name", "First Name", "Title", "Title of Courtesy",
              "Birth Date", "Hire Date", "Address", "City", "Region", "Postal Code",
              "Country", "Home Phone", "Extension", "Photo", "Notes"
          ]
          for field, value in zip(fields, employee):
              print(f"{field}: {value}")

          input("\nPress Enter to continue...")
          return
  
  def add_employee(self,last_name, first_name, title, title_of_courtesy, birth_date, hire_date, address, city, region, postal_code, country, home_phone, extension, photo, notes):
    query = """
      INSERT INTO employees (last_name, first_name, title, title_of_courtesy, birth_date, hire_date, address, city, region, postal_code, country, home_phone, extension, photo, notes)
      VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    self.db.cursor.execute(query, (last_name, first_name, title, title_of_courtesy, birth_date, hire_date, address, city, region, postal_code, country, home_phone, extension, photo, notes))
    self.db.connection.commit()
    print(f"Employee {title_of_courtesy} {first_name} {last_name} has been added successfully")
  
  def delete_employee(self, employee_id, title_of_courtesy, first_name, last_name):
    employees = self.view_employees()

    if not employees:
      return
    
    confirm = input(f"Are you sure you want to delete employee '{title_of_courtesy}. {first_name} {last_name}' (y/n): ").lower().strip()
    
    if confirm != 'y':
      print("Deletion cancelled")
      return
    try:
      query = "DELETE FROM employees WHERE employee_id = %s"
      self.db.cursor.execute(query, (employee_id, ))
      self.db.connection.commit()

      if self.db.cursor.rowcount > 0:
        print(f"Employee '{title_of_courtesy}. {first_name} {last_name}' has been deleted.")
      else:
        print(f"No employee found with ID {employee_id}.")
    except Exception as e:
      print(f"Error happened while deletion: {e}")


  
