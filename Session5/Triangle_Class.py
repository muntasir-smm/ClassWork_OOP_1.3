'''
Write Python programs for creating following classes and their objects:

4. Triangle Class
'''
import math
class Triangle:
    def __init__(self,base,height,area,peri):
        self.base=base
        self.height=height
        self.area=area
        self.peri=peri
    

def main():
    b=float(input("Enter base:"))
    h=float(input("Enter height:"))
    a=0.5*b*h
    hyp = math.sqrt(b**2 + h**2)
    p = b + h + hyp

    rec1=Triangle(b,h,a,p)
    print(f"base: {rec1.base}\nheight: {rec1.height}\narea: {rec1.area}\nperi: {rec1.peri:.4f}")

main()