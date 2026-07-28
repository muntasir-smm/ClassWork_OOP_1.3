class Student:
    count_student=0

    @classmethod
    def total_student(std):
        print(f"Total students: {Student.count_student}")

    def __init__(self,name,Id,gpa,Dept):
        self.name=name
        self.Id=Id
        self.gpa=gpa
        self.Dept=Dept
        Student.count_student +=1

    # Behavior of an object
    def student_info(self):
        print(f"Name: {self.name}, ID: {self.Id}, GPA:{self.gpa}, Dept: {self.Dept} \n")

def main():
    std1=Student("Munna",319,3.7,"CSE")
    std2=Student("Munna",319,3.7,"CSE")
    std3=Student("Munna",319,3.7,"CSE")
    std4=Student("Munna",319,3.7,"CSE")
    std1.student_info()
    Student.total_student()
main()