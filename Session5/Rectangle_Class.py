'''
Write Python programs for creating following classes and their objects:

3. Rectangle Class
'''

class Rectangle:
    def __init__(self,length,width,area,peri):
        self.length=length
        self.width=width
        self.area=area
        self.peri=peri
    

def main():
    l=float(input("Enter length:"))
    w=float(input("Enter width:"))
    a=l*w
    p=2*(l+w)

    rec1=Rectangle(l,w,a,p)
    print(f"length: {rec1.length}\nwidth: {rec1.width}\narea: {rec1.area}\nperi: {rec1.peri}")

main()