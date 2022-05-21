num= integer
print (int (input ('a number for choose a option =', num)))


print(' for calculating table = 1 /n for perfect number = 2 /n for prime number = 3  /n for reverse number = 4  /n for Armstrong number = 5 /n for fibanocci series = 6 /n for simple interest = 7 /n for area of circle = 8 /n for area of rectangle = 9 /n for add , subtract , multiplye and segment = 10") 



if num == 1 
a = int(input'which number table u want = ')
for i in the range (1, 11 )
print (' a, 'x', i ,'=', a*i' )


elif num == 2
i = 1
sum = 0
 n= int(input' enter a number = ' )
 while i < n
 if  n % i == 0
  sum =sum + i 
  i  += 1
  if sum == n
     print(i , 'is a perfect number' )
  else :
      print (i ,' is not a perfect number')
      
      
elif num == 3
count = 0
n= int (input('enter a number = ' ))
for i  in range (i, n+ i )
if n % i == 0
count += 1
if count == 2
print(n, " is a prime number")
else:
    print(n, " is not a prime number" )
    
 
 
elif num == 4
num = int(input("enter a number for reverse = "))
rev = 0
while( num !=0)
rev = rev * 10
rev = rev + num % 10
num = num // 10
print("reverse number = " , rev)


elif num == 5
num = int(input("enter a number "))
sum = 0
temp = num
while temp > 0 
digit = temp %  10
sum += digit ** 3
 temp //= 10
 
 if num == sum
 print(num, "is an Armstrong num" )
 else:
     print(num, " is an Armstrong num " )
     
elif num == 6
nterms = int(input(" how many terms you want= "))
n1 = 0
n2 = 1 
count = 2
if nterms <= 0
print ( "plz enter a positive number= ")
elif:
    nterms == 1
    print(" Fibonacci series = n1 ")
    else:
        print(" Fibonacci series = )
        print(n1," ," ,n2, end= ' , ')
        while count< nterms
        nth = n1 + n2
        print(nth,end=' , ')
        n1 = n2
        n2 = nth
        count += 1
    
     
 
