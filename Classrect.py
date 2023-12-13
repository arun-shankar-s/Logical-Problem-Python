class Rectangle:
    
    def area(self):
          a=int(input("Enter the length"))
          b=int(input("Enter the breadth"))
          c=a*b
          print(c)
          return c
          
            

obj=Rectangle()
a1=obj.area()
a2=obj.area()

if a1>a2:
     print("First Rectangle is bigger")
else:
     print("Second Rectangle is bigger")




