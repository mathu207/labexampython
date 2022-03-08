a=input("area of the triangle")
a=float(input("Enter the length of 1st side"))
b=float(input("Enter  the length of 2nd side"))
c=float(input("Enter  the length of 3rd side"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))*1/2
print("The area of the triangle is %.2f"%area)
b=input("area of the circle")
PI=3.14
r=float(input("Enter the radius of a circle:"))
area=PI*r*r
print("Area of a circle=%.2f"%area)
c=input("area of rectangle")
l=float(input("Enter the length of a Rectangle"))
b=float(input("Enter the breadth of a Rectangle"))
area=l*b
print("Area of a Rectangle is=%.2f"%area)
