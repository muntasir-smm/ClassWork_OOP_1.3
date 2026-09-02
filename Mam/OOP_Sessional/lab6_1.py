#Class, Object

#This is a student class
class Student: 
    def __init__(self, name, stID, GPA):
        self.name = name
        self.stID = stID
        self.GPA = GPA
    def greet(self):
        print(f"Hello {self.name}, welcome to this class!")

#this is the main function for creating new objects of class Student
def main():
    student = Student("Rafi", 202610256, 3.5)
    #student is an object of Student class
    print(student.name)
    student.greet()
#main function is called here
main()