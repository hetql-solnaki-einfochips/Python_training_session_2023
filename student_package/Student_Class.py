class Student:
    school_name=None
    school_address=None

    def __int__(self):
        self.student_name=None
        self.student_id=None
        self.student_roll_no=None
        self.student_percentage=None

    # DYnammic methos
    def student_details(self):
        print(30 * '-')
        print("Student name", self.student_name)  # Dynamic variable call with object name and here self is the object
        print("Student Id", self.student_id)  # Dynamic variable call with object name and here self is the object
        print("Student Roll No", self.student_roll_no)  # Dynamic variable call with object name and here self is the object
        print("Student Percentage", self.student_percentage)
        print("School name", Student.school_name)  # STatic variable call with class name
        print("School location", Student.school_address)  # STatic variable call with class name
        print(30 * '-')

    def assign_new_value(self):
        print(30 * '+')
        print("New valuesas per below")
        print(30 * '+')
        self.student_name="Hetal"
        print(self.student_name)
        self.student_id="hetal@gmail.com"
        print(self.student_id)
        self.student_roll_no=9001
        print(self.student_roll_no)
        self.student_percentage=57.6
        print(self.student_percentage)
        print(30 * '-')
