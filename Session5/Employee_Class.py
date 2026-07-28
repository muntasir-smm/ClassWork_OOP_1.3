'''
Write Python programs for creating following classes and their objects:

6. Employee Class

'''

class Employee:
    def __init__(self,name,ID,Salary):
        self.name=name
        self.ID=ID
        self.Salary=Salary

def main():
    emp1=Employee("Munna",319,"37K")
    print(f"Name:{emp1.name}\nID:{emp1.ID}\nSalary: {emp1.Salary}")
main()
