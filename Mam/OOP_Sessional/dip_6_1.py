#define a class
#class keyword classname:
class Student:
    #constructor
    def __init__(self, ID, name, gpa, dept):
        self.ID = ID
        self.name = name
        self.gpa = gpa
        self.dept = dept
    #member function    
    def admit(self):
        print(f"welcome {self.name} to our department {self.dept}")

def main():
    newstd = Student(202630120, "Rafiq", 3.5, "CSE")
    newstd1 = Student(202630250, "Rafi", 3.6, "BBA")
    print(newstd.gpa)
    print(newstd.name)
    print(newstd.dept)
    newstd.admit()
    newstd1.admit()

main()
