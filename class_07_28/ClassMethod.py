class Student:
    count_student=0

    @classmethod
    def total_student(std):
        print(f"Total students: {Student.count_student}")

    def __init__(self,name,Id,gpa,Dept):
        self.name=name
        self.Id=Id
        self.__gpa=gpa
        self.Dept=Dept
        Student.count_student +=1

    # Behavior of an object
    def student_info(self):
        print(f"Name: {self.name}, ID: {self.Id}, GPA:{self.__gpa}, Dept: {self.Dept} \n")

def main():
    std1=Student("Munna",319,3.7,"CSE")
    std2=Student("Sobuj",264,3.7,"CSE")
    std3=Student("Sabbir",100,3.7,"CSE")
    std4=Student("Mrinmoy",404,3.7,"CSE")
    std1.student_info()
    std2.student_info()
    std3.student_info()
    std4.student_info()
    Student.total_student()
main()