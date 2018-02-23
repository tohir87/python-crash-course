# simple scripts that demonstrates how a class works

class Student():
    # default constructor
    def __init__(self, first_name='', last_name='', student_number=0):
        # define student details
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number

    # method to print student data
    def printStudent(self):
        print(self.first_name, self.last_name)
        print(self.student_number)



a = Student()
a.first_name = 'Tohir'
a.last_name = 'Omoloye'
a.student_number = '29574'

a.printStudent()

b = Student('Farida', 'Umar', '2554244')
b.printStudent()
