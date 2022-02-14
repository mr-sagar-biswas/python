# delete any file


def delete(a):
    import os
    if os.path.exists(a):
        os.remove(a)
    else:
        print("the file dosent exists")
    return(a)
y=input("location of the file you want to delete:")
z=input("name of the file you want to delete:")
x=input("type of the file you want to delete:")
delete(y+z+"."+x)