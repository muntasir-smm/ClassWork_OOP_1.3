#Encalpsulation

class Student:
    def __init__(self,name,Id,gpa,Dept):
        self.name=name
        self.Id=Id
        self.gpa=gpa
        self.Dept=Dept

    # Behavior of an object
    def student_info(self): #function
        print(f"Name: {self.name}, ID: {self.Id}, GPA:{self.gpa}, Dept: {self.Dept} \n")

class Teacher:
    def __init__(self,name,ID,salary,Dept):
        self.name=name
        self.ID=ID
        self.salary=salary
        self.Dept=Dept

    # Behavior of an object
    def teacher_info(self): #function
        print(f"Name: {self.name}, ID: {self.ID}, Dept.:{self.Dept}, salary: {self.salary} \n")

class Course:
    def __init__(self,Title,code,Creadit,Dept):
        self.Title=Title
        self.code=code
        self.Creadit=Creadit
        self.Dept=Dept

    def course_info(self):
        print(f"Title: {self.Title}, Code: {self.code}, Creadit: {self.Creadit}, Dept.:{self.Dept} \n")

def main():
    std1=Student("Munna",319,3.7,"CSE")
    std1.student_info()

    tech1=Teacher("Munna",319,"50K","CSE")
    tech1.teacher_info()

    course1=Course("OOP",2324,3,"CSE")
    course1.course_info()

main()