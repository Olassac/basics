Breadth=int(input("collect the breadth of a rectangle"))
Length=int(input("collect the length of the rectangle"))
Base=int(input("collect the base of the triangle"))
Height=int(input("collect the height of the height"))

def Rectangle(B,L):
    result= B*L
    print(result)
def Triangle(Base, Height):
    result=Base*Height/2
    print(result)


Rectangle(Breadth,Length)
Triangle(Base,Height)
