class Tme:
    def __init__(self):
        self.__hour=0
        self.__minute=0
        self.__second=0

    def set_time(self):
        x,y,z=map(int,input("Enter the time in (hh:mm:ss) format").split(":"))
        self.__hour=x
        self.__minute=y
        self.__second=z
    def __add__(self,other):
        c=Tme()
        c.__hour = self.__hour + other.__hour
        c.__minute = self.__minute + other.__minute
        c.__second = self.__second + other.__second
        if (c.__second>=60):
            c.__second=c.__second-60
            c.__minute=c.__minute+1
        if(c.__minute>=60):
            c.__minute=c.__minute-60
            c.__hour=c.__hour+1
        return c
    def display(self):
        print("Time:",self.__hour,":",self.__minute,":",self.__second)

a=Tme()
a.set_time()

b=Tme()
b.set_time()

c=a+b
c.display()
