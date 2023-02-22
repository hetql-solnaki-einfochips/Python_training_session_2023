from Demo4_emp.Emp_class import Employee

Employee.compny_name= "Einfochips"
Employee.compny_location = "Ahmedabad"

#STatic variable with class name
print(Employee.compny_name)
print(Employee.compny_location)

emp1=Employee()
emp2=Employee()
emp3=Employee()

emp1.emp_id=11
emp1.emp_name='Paul'
emp1.emp_salary=500

emp2.emp_id=10
emp2.emp_name='kim'
emp2.emp_salary=900

emp3.emp_id=13
emp3.emp_name='Jazz'
emp3.emp_salary=800

print(emp1.emp_id)
print(emp2.emp_id)
print(emp3.emp_id)

#Static method call with class name
Employee.author_name()

#Dynamic method call with object name
emp1.print_details_nonstatic()
emp2.print_details_nonstatic()
emp3.print_details_nonstatic()

print("Count details")
emp1.count_emp_details()
emp2.count_emp_details()
emp3.count_emp_details()



