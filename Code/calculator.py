from array import*

import math
##############################



def perimeter():
	
	print("\n\n\t\tCALCULATE  PERIMETER OF DIFFERENT  SHAPES\n")
	P=["Square","Rectangle","Triangle","Circle","Semicircle","Sector of Circle","parallelogram","Trapezium","Kite","Cube","Cuboid"]
	for i in range(1,12):
		print(i,"--",P[i-1])
	
	p=int(input("\nEnter your choice( 1-to-11 ) = "))

	if p==1:
		print("\nPerimeter of Square = 4 × Side\n SO , you need to \n")
		s=float(input("Enter Side = "))
		print("\nPerimeter of Square = ",4*s)
		
	elif p==2:
		print("\nPerimeter of Rectangle = 2 × ( Length + Breadth )\n SO , you need to \n")
		L=float(input("Enter Length = "))
		B=float(input("Enter Breadth = "))
		print("\nPerimeter of Rectangle = ",2*(L+B))
		
	elif p==3:
		print("\nPerimeter of Triangle = Side-1 + Side-2 + Side-3 \n SO , you need to \n")
		S1=float(input("Enter Side-1 = "))
		S2=float(input("Enter Side-2 = "))
		S3=float(input("Enter Side-3 = "))
		print("\nPerimeter of Triangle = ",S1+S2+S3)
		
	elif p==4:
		print("\nPerimeter of Circle = 2 × π × Radius \n SO , you need to \n")
		r=float(input("Enter Radius = "))
		print("\nPerimeter of Circle = ",2*3.14*r )
		
	elif p==5:
		print("\nPerimeter of Semiircle = (π × Radius) + ( 2 × Radius )\n SO , you need to \n")
		r=float(input("Enter Radius = "))
		print("\nPerimeter of Semicircle = ",3.14*r + 2*r)
		
	elif p==6:
		print("\nPerimeter of Sector = (  2 × π × Radius × Angle  ) + () 2 × Radius )\n\t\t\t\t\t  -----\n\t\t\t\t\t   360\n SO , you need to \n")
		r=float(input("Enter Radius = "))
		q=float(input("Enter Angle of Sector = "))
		print("\nPerimeter of Sector = ",(2*3.14*r*q/360) + 2*r)
		
	elif p==7:
		print("\nPerimeter of Parallelogram = 2 × (Sum of Length of Parallel Sides)\n SO , you need to \n")
		s1= float(input("Enter Length of 1st Set of parallel Sides = "))
		s2= float(input("Enter Length of 2nd Set of parallel Side = "))
		print("\nPerimeter of Parallelogram = ",2*(s1+s2))
		
	elif p==8:
		print("\nPerimeter of Trapezium = Side-1 + Side-2 + Side-3 + Side-4\n SO , you need to \n ")
		s1 = float(input("Enter Length of Side-1 = "))
		s2 = float(input("Enter Length of Side-2 = "))
		s3 = float(input("Enter Length of Side-3 = "))
		s4 = float(input("Enter Length of Side-4 = "))
		print("\nPerimeter of Trapezium = ", s1+s2+s3+s4)
		
	elif p==9:
		print("\nPerimeter of Kite = 2 × (Sum of 2 Pair of Equal Sides)\n SO , you need to \n")
		s1=float(input("Enter Length of 1st Pair of Equal Sides = "))
		s2=float(input("Enter Length of 2nd Pair of Equal Sides = "))
		print("\nPerimeter of Kite= ",2*(s1+s2))
		
	elif p==10:
		print("\nPerimeter of Cube = 12 × Side\n SO , you need to \n")
		s=float(input("Enter Side = "))
		print("\nPerimeter of Cube = ",12*s)
		
	elif p==11:
		print("\nPerimeter of Cuboid = 4 × ( Length + Breadth + Height )\n SO , you need to \n")
		l=float(input("Enter Length = "))
		b=float(input("Enter Breadth = "))
		h=float(input("Enter Height = "))
		print("\nPerimeter of Cuboid = ",4*(l+b+h))
		
	m=input("\nWant to Calculate More Area (yes/no) = ").lower()
	if m=="yes" :
		perimeter()




###############################




def area2d():
	
	print("\n\n\t\tCALCULATE  AREA  OF  2-D  SHAPES\n")
	S=["Square","Rectangle","Circle","Triangle","Trapezium","Parallelogram","kite"]
	for i in range(1,8):
		print(i,"..",S[i-1])
	
	C=int(input("Enter your choice(1-to-7)="))
	
	if C==1:
		print("\nArea of Square = Side × Side\n SO , you need to \n")
		s=float(input("Enter Side = "))
		print("\nArea = ",s*s)
		
	elif C==2:
		print("\nArea of Rectangle = Length × Breadth\n SO , you need to \n")
		L=float(input("Enter Length = "))
		B=float(input("Enter Breadth = "))
		print("\nArea = ",L*B)
		
	elif C==3:
		print("\nArea of Circle = π × Radius ²\n SO , you need to \n")
		r=float(input("Enter Radius = "))
		print("\nArea= π × r × r=",3.14*r*r )
		
	elif C==4:
		print("\nArea of Triangle = 1 × Base × Height \n\t\t  --- \n\t\t   2 \n SO , you need to \n")
		B=float(input("Enter Base= "))
		H=float(input("Enter Height = "))
		print("\nArea = ",B*H*1/2)
		
	elif C==5:
		print("\nArea of Trapezium = Base-1 + Base-2 × Height \n\t\t    ---------------\n\t\t           2\n SO , you need to \n ")
		h = float(input("Enter Height = "))
		b1 = float(input("Enter Base-1 = "))
		b2 = float(input("Enter Base-2 = "))
		print("\nArea = ", ((b1 + b2) / 2) * h)
	elif C==6:
		print("\nArea of Parallelogram = Base × Height \n SO , you need to \n")
		B= float(input("Enter Base = "))
		H= float(input("Enter Height = "))
		print("\nArea = ",B*H)
		
	elif C==7:
		print("\nArea of Kite = Diagonal-1 × Diagonal-2\n\t\t---------------------\n\t\t\t  2\n SO , you need to \n")
		d=float(input("Enter Diagonal-1 = "))
		D=float(input("Enter Diagonal-2 = "))
		print("\nArea = ",d*D*1/2)
		
	def choose1():
		m=input("\nWant to Calculate More Area (yes/no) = ").lower()
		if (m=="yes" or m=="no"):
			if m=="yes" :
				area2d()
		else :
			print("\n\t\tWRONG CHOICE")
			choose1()
	choose1()





##############################




def area3d():
	
	print("\n\n\t\tCALCULATE  AREA  OF  3-D  SHAPES\n")
	S=["TSA-Cube","LSA-Cube","TSA-Cuboid","LSA-Cuboid","TSA-Cone","CSA-Cone","TSA-Frustum of cone","CSA-Frustum of Cone","TSA-Cylinder","CSA-Cylinder","TSA-Sphere","TSA-Hemisphere","CSA-Hemisphere"]
	
	for i in range(1,14):
		print(i,"..",S[i-1])
	
	C=int(input("\nEnter your choice(1-to-13)="))
	
	if C==1:
		print("\nTSA-Cube = 6 × Side × Side \n SO , you need to -\n")
		S= float(input("Enter any Side = "))
		print("\n\tTSA-Cube=",6*S*S)
		
	elif C==2:
		print("\nLSA-Cube = 4 × Side × Side \n SO , you need to -\n")
		S= float(input("Enter any Side = "))
		print("\n\tLSA-Cube=",4*S*S)
		
	elif C==3:
		print("\nTSA-Cuboid = 2 × (Length × Width + Width × Height + Height × Length)\n SO , you need to-\n")
		l= float(input("Enter Length = "))
		w= float(input("Enter Width = "))
		h= float(input("Enter Height = "))
		print("\n\tTSA-Cuboid = ",2*(l*w+w*h+h*l))
		
	elif C==4:
		print("\nLSA-Cuboid = 2 × Height × (Length + Width)\n SO , you need to-\n")
		l= float(input("Enter Length = "))
		w= float(input("Enter Width = "))
		h= float(input("Enter Height = "))
		print("\n\tLSA-Cuboid = ",2*h*(l+w))
		
	elif C==5:
		print("\nTSA-Cone = π × Radius × (Radius × Slant Height)\n\nAlso ; Slant Height = √ (Raxius × Radius + Height × Height)\n\n SO , you need to enter\n")
		r=float(input("Enter Radius = "))
		h=float(input("Enter Height = "))
		l = math.sqrt(r* r + h* h)
		print("\n\tLength of a Side (Slant)of a Cone = ", l)
		print("\tTSA-Cone = " ,3.14 * r * (r + l))
		
	elif C==6:
		print("\nCSA-Cone = π × Radius × Slant Height\n\nAlso ; Slant Height = √ (Raxius × Radius + Height × Height)\n\n SO , you need to enter\n")
		r=float(input("Enter Radius = "))
		h=float(input("Enter Height = "))
		l = math.sqrt(r* r + h* h)
		print("\n\tLength of a Side (Slant)of a Cone = ", l)
		print("\n\tCSA-Cone = " ,3.14 * r * l)
		
		
	elif C==7:
		print("\nTSA-Frustum of Cone = π × Slant Height × (Radius-1 + Radius-2) + π ( Radius-1 ² + Radius-2 ²)\n\nAlso ; Slant Height = √((Radius-1 - Radius-2)² + Height²)\n\n SO , you need to-\n")
		r1=float(input("Enter Radius-1(Grater) = "))
		r2=float(input("Enter Radius-2 (Smaller)= "))
		h=float(input("Enter Height = "))
		l = math.sqrt((r1-r2)*(r1-r2) + h* h)
		print("\n\tLength of a Side (Slant)of a Cone = ", l)
		print("\tTSA-Frustum of Cone = " ,3.14 * l * (r1 + r2)+3.14*(r1*r1+r2*r2))
		
	elif C==8:
		print("\nCSA-Frustum of Cone = π × Slant Height × (Radius-1 + Radius-2)\n\nAlso ; Slant Height = √((Radius-1 - Radius-2)² + Height²)\n\n SO , you need to-\n")
		r1=float(input("Enter Radius-1(Grater) = "))
		r2=float(input("Enter Radius-2 (Smaller)= "))
		h=float(input("Enter Height = "))
		l = math.sqrt((r1-r2)*(r1-r2) + h* h)
		print("\n\tLength of a Side (Slant)of a Cone = ", l)
		print("\tCSA-Frustum of Cone = " ,3.14 * l * (r1 + r2))
		
	elif C==9:
		print("\nTSA-Cylinder = 2 × π × Radius (Radius + Height)\n SO , you need to -\n")
		r=float(input("Enter Radius = "))
		h=float(input("Enter Height = "))
		print("\n\tTSA- Cylinder = ",2*3.14*r*(r+h))
		
	elif C==10:
		print("\nCSA-Cylinder= 2 × π × Radius × Height \n SO , you need to -\n")
		r=float(input("Enter Radius = "))
		h=float(input("Enter Height = "))
		print("\n\tCSA- Cylinder = ",2*3.14*r*h)
		
	elif C==11:
		print("\nTSA-Sphere = 4 × π × Radius ²\ n SO , you need to-\n")
		r= float(input("Enter Radius = "))
		print("\n\tTSA-Sphere =",4*3.14*r*r)
		
	elif C==12:
		print("\nTSA-Hemisphere = 3 × π × Radius ²\ n SO , you need to-\n")
		r= float(input("Enter Radius = "))
		print("\n\tTSA-Hemisphere = ",3*3.14*r*r)
		
		
	elif C==13:
		print("\nTSA-Hemisphere = 2 × π × Radius ²\ n SO , you need to-\n")
		r= float(input("Enter Radius = "))
		print("\n\tCSA-Hemisphere = ",2*3.14*r*r) 
		
	def choose2():
		m=input("\nWant to Calculate More Area (yes/no) = ").lower()
		if (m=="yes" or m=="no"):
			if m=="yes" :
				area3d()
		else :
			print("\n\t\tWRONG CHOICE")
			choose2()
	choose2()





###############################




def Volume():
		
		print("\n\n\t\tCALCULATE  VOLUME\n")
		V=["Cube","Cuboid","Cone","Frustum of Cone","Cylinder","Sphere","Hemisphere"]
		
		for i in range(1,8):
			print(i,"..",V[i-1])
		
		C=int(input("\nEnter your choice(1-to-7)="))
		
		if C==1:
			print("\nVolume of Cube = Side × Side × Side = Side ³ \n SO , you need to -\n")
			S= float(input("Enter any Side = "))
			print("\n\nVolume of Cube=",S*S*S)
			
		elif C==2:
			print("\nVolume of Cuboid = Length × Width × Height\n SO , you need to-\n")
			l= float(input("Enter Length = "))
			w= float(input("Enter Width = "))
			h= float(input("Enter Height = "))
			print("\n\tVolume of Cuboid = ",l*w*h)
			
		elif C==3:
			print("\nVolume of Cone = π × Radius ² × Height\n\t\t\t\t------\n\t\t\t\t  3\n\n SO , you need to enter\n")
			r=float(input("Enter Radius = "))
			h=float(input("Enter Height = "))
			print("\tVolume of Cone = " ,3.14*r*r*h*1/3)
			
		elif C==4:
			print("\nVolume of Frustum of Cone = 1 × π × Height × (Radius-1 ² + Radius-1 × Radius-2 + Radius-2 ²)\n\t\t\t   ---\n\t\t\t    3\n\n SO , you need to-\n")
			r1=float(input("Enter Radius-1 = "))
			r2=float(input("Enter Radius-2 = "))
			h=float(input("Enter Height = "))
			print("\tTSA-Frustum of Cone = " ,1/3*3.14 * h * (r1*r1+r1*r2+r2*r2))
				
		elif C==5:
			print("\nVolume of Cylinder = π × Radius ² × Height \n SO , you need to -\n")
			r=float(input("Enter Radius = "))
			h=float(input("Enter Height = "))
			print("\n\tVolume of Cylinder = ",3.14*r*r*h)
			
		elif C==6:
			print("\nVolume of Hemisphere = 4 × π × Radius ³\nn\t\t      ---\n\t\t       3\n SO , you need to-\n")
			r= float(input("Enter Radius = "))
			print("\n\tVolume of Hemisphere = ",4/3*3.14*r*r*r)
			
		elif C==7:
			print("\nVolume of Hemisphere = 2 × π × Radius ³\nn\t\t      ---\n\t\t       3\n SO , you need to-\n")
			r= float(input("Enter Radius = "))
			print("\n\tVolume of Hemisphere = ",2/3*3.14*r*r*r)
			
			
		
		def choose3():
			m=input("\nWant to Calculate More Volume (yes/no) = ").lower()
			if (m=="yes" or m=="no"):
				if m=="yes" :
					Volume()
			else :
				print("\n\t\tWRONG CHOICE")
				choose3()
		choose3()





###############################


def Calculator():

	print("\n\n\t\tMUKUL'S  CALCULATOR")

	print("WHAT YOU WANT TO CALCULATE\n")

	Q=["Perimeter","2-D Shapes Area","3-D Shapes Area","Volume","Percentage","Average","Simple Interest","Evaluate Expression","Evaluate Power","Converter","Trignometric Functions Value"]

	for j in range(1,12):
		print(j,"--",Q[j-1])
	c=int(input("Enter Your Choice(1-to-11)="))
	
	if c==1:
		perimeter()
	
	elif c==2:
		area2d()
	
	elif c==3:
   	 area3d()
    
	elif c==4:
		Volume()
	
	elif c==5:
		print("For Percentage")
		t=float(input("Total value="))
		o=float(input("Occupied="))
		print("Percentage=Occupied × 100/Total=",o/t*100,"%")
	
	elif c==6:
		print("For Average")
		t=int(input("Enter total no of enteries="))
		e=array('f',[])
		T=0
		for i in range(t):
				v=float(input("enter value="))
				e.append(v)
				T=T+e[i]
		print("Average=",T/t)
	
	elif c==7:
		print("For Simple Interest")
		p=float(input("Enter principal amount="))
		r=float(input("Enter interest rate="))
		t=int(input("Enter time (in years)="))
		print("Simple Interest=",p*r*t/100,"\nAmount=",(p+p*r*t/100))
	
	elif c==8:
		print("\n\nFor Solving Expression like ' 2+9/3*2 = 8 ' \n\n SO , you need to-")
		R=float(eval(input("Enter Your Expression = ")))
		print("Result = ",R)
	
	elif c==9:
		print("\n\nFor Calculating Power Of a Number\n\nYou need to-")
		N=float(input("Enter Your Number = "))
		P=float(eval(input("Enter Power = ")))
		print("Result = ",N**P)
		
	elif c==10:
		print("\n\t\t\t\tCONVERTER \n\n\t\t\t WORK IN PROGRESS")
	
	elif c==11:
		print("\n\t\tTrignometric Function Value Calculator \n\n\t\tWORK IN PROGRESS")
	
	def choose4():
				m=input("\nWant to Perform More Calculations in Mukul's Calculator (yes/no) = ").lower()
				if (m=="yes" or m=="no"):
					if m=="yes" :
						Calculator()
				else :
					print("\n\t\tWRONG CHOICE")
					choose4()
	choose4()
Calculator()
	
