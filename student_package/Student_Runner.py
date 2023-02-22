from student_package.Student_Class import Student

Student.school_name="DPS"
Student.school_address="Ahmedabad"

std1=Student()
std2=Student()
std3=Student()

std1.student_id= 'jack@gmail.com'
std1.student_name='Jack'
std1.student_roll_no= 1001
std1.student_percentage=45.2

std2.student_id= 'peter@gmail.com'
std2.student_name='peter'
std2.student_roll_no= 1002
std2.student_percentage=85.2

std3.student_id= 'mark@gmail.com'
std3.student_name='mark'
std3.student_roll_no= 1003
std3.student_percentage=56.5

#Print the mailid for each instance and run the code.
print("Email id for student 1",std1.student_id)
print("Email id for student 2",std2.student_id)
print("Email id for student 3",std3.student_id)

std1.student_details()
std2.student_details()
std3.student_details()

std1.assign_new_value()

print("Email id for student 1",std1.student_id)
print("Email id for student 2",std2.student_id)
print("Email id for student 3",std3.student_id)