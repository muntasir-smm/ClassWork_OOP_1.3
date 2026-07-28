'''
Write Python programs for creating following classes and their objects:

5. Student Class

'''

class Student:
    def __init__(self,name,stID,CGPA):
        self.name=name
        self.stID=stID
        self.CGPA=CGPA

def main():
    student=Student("Munna",319,3.7)
    print(f"Name:{student.name}\nID:{student.stID}\nCGPA: {student.CGPA}")
main()
