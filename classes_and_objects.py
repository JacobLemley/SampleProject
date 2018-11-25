print("================Classes and Objects================")
#"classes and objects create your own data types"
# a class defines your own data type (defines what a student is)
# an object is an actual iteration of that class
#student.py defines the student class
from student import Student

student1 = Student("Jim", "Philosophy", 3.1, False) #this creates a student object
student2 = Student("Pam", "Art", 2.0, True) #this creates a student object

print(student1.name)
print(student2.gpa)


print("================Classes and Objects================")
