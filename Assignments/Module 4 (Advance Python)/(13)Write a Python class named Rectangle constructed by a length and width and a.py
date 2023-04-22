#Write a Python class named Rectangle constructed by a length and width and a
#methodwhich will compute the area of a rectangle.

class Rectangle:
    length=0
    width=0
    def area(self,length,width):
        return length*width
obj=Rectangle()
x=int(input("Enter Length of the Rectangle:"))
y=int(input("Enter width of the Rectangle:"))
print("Area of a Rectangle :",obj.area(x,y))
    
