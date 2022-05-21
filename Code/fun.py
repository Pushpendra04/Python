print("Details")
a=int(input("Enter id = "))
b=input("Enter name = ")
c=int(input("Enter age = "))
d=input("Enter City = ")
e=int(input("Enter pincode = "))
f=input("Enter Qualification = ")

g=int(input("What do you want to perform ?\n1 - Find\n2 - Update\n3 - Remove\n"))
if g==1:
    o=int(input("id"))
    if o==a:
        print("yes")
    else:
        print("No")
              
elif g==2:
    t=int(input("What do you want to update ?\n1 - id\n2 - name\n3 - age\n4 - city\n5 - pincode\n6 - qualification\n"))
    if t==1:
        p=int(input("Enter id = "))
        a=p;
        print(a)
    elif t==2:
        k=input("Enter name = ")
        b=k;
        print(b)
    elif t==3:
        h=int(input("Enter age = "))
        c=h;
        print(c)
    elif t==4:
        g=input("Enter City = ")
        d=g;
        print(d)
    elif t==5:
        x=int(input("Enter pincode = "))
        e=x;
        print(e)
    elif t==6:
        z=input("Enter Qualification = ")
        f=z;
        print(z)

elif g==3:
    t=int(input("What do you want to delete ?\n1 - id\n2 - name\n3 - age\n4 - city\n5 - pincode\n6 - qualification\n"))
    name=[a,b,c,d,e,f]
    if t==1:
        name.remove(a)
        print("deleted")
    elif t==2:
        name.remove(b)
        print("deleted")
    elif t==3:
        name.remove(c)
        print("deleted")
    elif t==4:
        name.remove(d)
        print(deleted)
    elif t==5:
        name.remove(e)
        print("deleted")
    elif t==6:
        name.remove(f)
        print("deleted")
    
        
        
        
        
        
    
    
