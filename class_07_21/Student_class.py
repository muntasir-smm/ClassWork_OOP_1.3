# Class, Object

class Student:
    def __init__(self,name,stID,CGPA):
        self.name=name
        self.stID=stID
        self.CGPA=CGPA

def main():
    student=Student("Munna",319,3.7)
    print(f"Name:{student.name},ID:{student.stID}")
main()
