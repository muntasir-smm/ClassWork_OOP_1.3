# For multiple variables

class Summation:
    def sum(self, *args):
        count=0
        for x in args:
            count +=x
        print("Total ",count)

    def maximum(self, *args):
        n=args[0]
        for x in args:
            if x>n:
                n=x
        print("Maximum ",n)
        
sum1=Summation()
sum1.sum(2,3,4,5)
Summation().maximum(2,6,3,7,9,1)