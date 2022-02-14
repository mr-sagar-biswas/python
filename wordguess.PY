import random
w=["cat","dog","mouse","snake","lion"]
rw=random.choice(w)
n=input("ENTER YOUR NAME:")
print("GOOD LUCK:",n)
q=0
while q<5:
    x=input("GUESS THE ANIMAL:")
    if x!=rw:
        print("WRONG")
        print("NUMBER OF FAILURE:",q+1)
        print("GUESSES LEFT:",5-q-1)
        q+=1
    elif x==rw:
        print("CONGRATS YOU GUESSED THE ANIMAL") 
        break
         