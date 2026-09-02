'''class Summation:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
            print("Total = ", s)
        elif a!=None and b!=None:
            s = a+b
            print("Total = ", s)
        else:
            print("Total = ", a)

sum1 = Summation()
sum1.sum(2)
sum1.sum(2, 3)
sum1.sum(2, 3, 4)'''

class Summation:
    def sum(self, *args):
        count = 0
        for x in args:
            count = count + x
        print("Total = ", count)

sum1 = Summation()
sum1.sum(2,3,4,5,6,6)
