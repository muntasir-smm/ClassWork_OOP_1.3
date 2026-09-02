class Robot:   #parent class
   def __init__(self, name):
      self.name = name
   def say_hi(self):
       print("Hi, I am " + self.name)
class PhysicianRobot(Robot): #child class
   pass

x = Robot("Wall-E")
y = PhysicianRobot("DocBot")

y.say_hi()    #inherited method invocation
x.say_hi()