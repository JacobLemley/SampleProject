#let's model a student:
class Student:

    def __init__(self, name, major, gpa, is_on_probation):     #creates initialize function which defines what a student is
    #when we create a student we are passing in the variables into the init function
        self.name = name    #this assigns the name of the student object to the name that we passed in
        self.major = major  #self refers to the actual object!
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    #we can put functions inside a class as well
    def on_honor_roll(self): #self is passed in first always
        if self.gpa >= 3.5:
            return True
        else:
            return False
