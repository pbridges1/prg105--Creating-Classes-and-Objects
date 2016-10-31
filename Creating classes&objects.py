#  Class
#     Student
# Attributes
#     studentID
#     first
#     last
#     email


class Student(object):
    """
    This class is meant to differentiate students from one another. This class holds student information of StudentID, First Name, Last Name, and Email
    """
student1 = Student()
student1.studentID = "B101"
student1.first = "Thomas"
student1.last = "Miller"
student1.email = student1.first + student1.last + "@python_center.org"

student2 = Student()
student2.studentID = "B201"
student2.first = "Paul"
student2.last = "Livingston"
student2.email = student2.first + student2.last + "@python_center.org"

student3 = Student()
student3.studentID = "B301"
student3.first = "Debra"
student3.last = "Warner"
student3.email = student3.first + student3.last + "@python_center.org"

print("Student ID: " + student1.studentID + "\n" + "First Name: " + student1.first + "\n" + "Last Name: " + student1.last + "\n" + "Email: " + student1.email)
print "\n"
print("Student ID: " + student2.studentID + "\n" + "First Name: " + student2.first + "\n" + "Last Name: " + student2.last + "\n" + "Email: " + student2.email)
print "\n"
print("Student ID: " + student3.studentID + "\n" + "First Name: " + student3.first + "\n" + "Last Name: " + student3.last + "\n" + "Email: " + student3.email)
