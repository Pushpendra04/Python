c=int(input("What do you want to perform ?\n1 - Insert\n2 - Read\n3 - Find\n4 - Update\n5 - Remove\n"))
def item(a,b,c,d,e,f):
 id=a;
 name=b;
 age=c;
 city=d;
 pincode=e;
 Qualification=f;
 print(id);
if c==1:
     
            a=int(input("Enter id = "))
            b=input("Enter name = ")
            c=int(input("Enter age = "))
            d=input("Enter City = ")
            e=int(input("Enter pincode = "))
            f=input("Enter Qualification = ")

         
                
                
        
elif c==2:
    
    item(a,b,c,d,e,f);
     


elif c==3:
    g=int(input("Enter the id ="))
    if g in name:
        print("Yes")
    else:
            print("No")
