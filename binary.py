#decimal to binary


o=100
while o>0:
    g=int(input("TYPE 1 TO RUN\nTYPE 0 TO EXIT\n"))
    if g==1:
        a=int(input("ENTER THE DECIMAL NUMBER:"))
        l=[]
        while a!=0:
            x=a%2
            l.append(int(x))
            y=(a-x)/2 
            a=y  
        l=l[::-1]
        print("\nTHE BINARY NUMBER IS:",end="")
        for i in l:
            print(i,end="")
        print("\n")  
    elif g==0:
        print("\n\nPROGRAM CLOSED\n\n") 
        break 
    else:
        print("\n\nUNRECOGNISED ENTRY\n\n")