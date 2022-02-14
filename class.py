#calculate using class and objects


class calculate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        z= self.x + self.y
        print("THE ADDITION IS:%5s"%z) 
    def subtract(self):
        z=self.x-self.y
        print("THE SUBTRACTION IS:%5s"%z)  
    def divide(self):
        z=self.x/self.y
        print("THE DIVISION IS:%5s"%z) 
    def multiply(self):
        z=self.x*self.y
        print("THE MULTIPLICATION IS:%5s"%z)
    def remainder(self):
        z=self.x%self.y
        print("THE REMAINDER IS:%5s"%z)
    def tothepower(self):
        z=self.x**self.y
        print("THE ANSWER IS:%5s"%z)                


a=float(input("ENTER THE FIRST NUMBER:"))
b=float(input("ENTER THE SECOND NUMBER:"))
print("FOR ADDITION TYPE:'a'\nFOR SUBTRACTION TYPE:'s'\nFOR DIVISION TYPE:'d'\nFOR MULTIPLICATIONTYPE:'m'\nFOR REMAINDERTYPE:'r'\nFOR TO THE POWER TYPE:'t'\n")
c=input("WHAT TO CALCULATE:")
num1=calculate(a,b)
if c=="a":
    P=num1.add()
elif c=="s":
    q=num1.subtract()
elif c=="d":
    P=num1.divide() 
elif c=="m":
    P=num1.multiply()      
elif c=="r":
    P=num1.remainder() 
elif c=="t":
    P=num1.tothepower() 