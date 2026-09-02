#encapsulation through classes
from datetime import date
class Student:
    count_student = 0
    
    @classmethod
    def total_student(std):
        print(f"Total number of admitted students: {Student.count_student}")
        

    def __init__(self, name, ID, gpa, dept, batch):
        self.name = name #attribute
        self.ID = ID
        self.gpa = gpa
        self.dept = dept
        self.batch = batch
        Student.count_student += 1
    
    #behavior of an object
    def student_info(self):
        print(f"Student Name: {self.name}, Student ID: {self.ID}, Dept: {self.dept}, Batch: {self.batch}, GPA:{self.gpa}")

    def getTA(self, obj, name):
        return obj.name


    
class Teacher:
    def __init__(self, name, ID, dept, salary):
        self.name = name
        self.ID = ID
        self.dept = dept
        self.salary = salary
    
    def teacher_info(self):
        print(f"Teacher's Name: {self.name}, Teacher's ID: {self.ID}, Dept: {self.dept}, Salary: {self.salary}")


class Course:
    def __init__(self, title, code, credit, dept):
        self.title = title
        self.code = code
        self.credit = credit
        self.dept = dept

    def course_info(self):
        print(f"Course Title: {self.title}, Course code: {self.code}, Credit Hour: {self.credit}, Dept: {self.dept}")

class Exam:
    def __init__(self, examdate, dept):
        self.__examdate = examdate
        self.dept = dept

    def exam_date(self):
        print(f"{self.dept} has exam on {self.__examdate}")


def main():
    std1 = Student("Khadiza", 202510253, 3.5, "CSE", 78)
    std1.student_info()
    
    std2 = Student("Muntasir", 202610252, 3.75, "BBA", 69)
    std2.student_info()

    std3 = Student("Muntasir", 202610252, 3.75, "BBA", 69)
    std4 = Student("Muntasir", 202610252, 3.75, "BBA", 69)
    

    ta1 = Teacher("Tahsin", 1025, "CSE", 500000)
    ta1.teacher_info()

    course1 = Course("OOP", "CSE 2312", 3.0, "CSE")
    course1.course_info()
    print(std4.getTA(ta1, "anyname"))

    exam1 = Exam(date(2026, 8, 15), "CSE")
    exam1.exam_date()

    Student.total_student()

main()
