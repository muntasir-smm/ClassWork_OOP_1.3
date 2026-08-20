class Robot:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi, I am " + self.name)

class Physician(Robot):
    def __init__(self, name, specialization):
        Robot.__init__(self, name)
        self.specialization = specialization
    def print_specialization(self):
        print("My specialization is " + self.specialization)
class Appointment(Physician):
    def __init__(self, name, specialization, schedule=None):
        Physician.__init__(self, name, specialization)
        self.schedule = schedule
        
    def get_schedule(self):
        print("Consultation Schedule: Monday & Wednesday: from 6:30 PM to 9:00 PM")

x = Appointment("DcoBot", "Neurology")
x.say_hi()
x.print_specialization()
x.get_schedule()
