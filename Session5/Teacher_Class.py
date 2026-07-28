'''
Write Python programs for creating following classes and their objects:

7. Teacher Class

'''

class Teacher:
    def __init__(self,name,ID,Salary):
        self.name=name
        self.ID=ID
        self.Salary=Salary

def main():
    teac1=Teacher("Munna",319,"37K")
    print(f"Name:{teac1.name}\nID:{teac1.ID}\nSalary: {teac1.Salary}")
main()
