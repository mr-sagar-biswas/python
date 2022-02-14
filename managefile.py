#manaage files using pythom

a=input("TYPE THE FILE LOCATION:")
b=input("NAME THE FILE:")
c=input("FYLE TYPE:")
e=input("WHAT TO WRITE:")
d=input("HOW MANY TIMES TO REPEAT:")
f =open(a+b+"."+c,"x")
f.close()
x=0
while x < int(d):
    f =open(a+b+"."+c,"a")
    f.write(e+"\n")
    f.close()
    x+=1