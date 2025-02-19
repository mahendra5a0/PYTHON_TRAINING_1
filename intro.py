'''print("hello guys")   #hello guys
print('hello guys')      #hello guys
print(hello guys)        #invalid syntax'''

'''  a=45
b=34
print("enter the values of a and b",a,b)#enter the values of a and b 45 34'''

#data types in python -->numbers,strings,booleans,list,tuples,sets,dictionaries
#numbers-->int,float,complex
#type of the variable is found by type(variable)
'''a=34
b=23.23
c=True
d=1+5j
e="laalasa"
f=[1,2,3]
print(a)
print(type(a)) #<class 'int'>
print(b)
print(type(b)) #<class 'float'>
print(c)
print(type(c)) #<class 'bool'>
print(d)
print(type(d)) #<class 'complex'>
print(e)
print(type(e)) #<class 'str'>
print(f)
print(type(f)) #<class 'list'>'''
#typecasting in python
'''x=34.32
c=int(x)
d=float(x)
print(c,d) # 34 34.32'''
#operators in python
#there are 6 types of operators in python
#1.Arithematic Operators
#2.Relational Operatos
#3.Logical Operatos
#4.Bitwise Operatos
#5.Assignment Operatos
#6.Special Operatos


#1.Arithematic Operators
'''a=4
b=56
print(a+b)      #60
print(a-b)      #-52
print(a*b)      #224
print(a/b)      #0.071428
print(a%b)      #4
print(a//b)     #0
print(a**b)     #51922968.......'''

#2.Relational Operators
'''a=34
b=23
print(a==b)    #False
print(a>b)     #True
print(a<b)     #False
print(a>=b)    #True
print(a<=b)    #False
print(a!=b)    #True'''

#3.Logical operators
'''x = 5
print(x > 3 and x < 10) #Returns True if both statements are true
print(x > 3 or x < 10) #Returns True if one of the statements is true
print(not(x > 3 and x < 10)) #Reverse the result, returns False if the result is true'''

#4.Bitwise Operators
'''print(6&3)   #2     #The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0   
print(6/3)   #7     #The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
print(6^3)   #5     #The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 
print(~6)    #-7    #add 1 and keep minus 
print(6<<3)  #48       #The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off
print(6>>3)  #0       #Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off'''


#5.Assignment Operators
'''x = 5
x += 3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=3
print(x)
x%= 3
print(x)
x//= 3
print(x)
x**= 3
print(x)
x&= 3
print(x)
x|= 3
print(x)
x^= 3
print(x)
x>>= 3
print(x)
x<<= 3
print(x)'''

#6.Special Operators
   #1.Membership Operators
'''in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y'''
   #2.Identity Operators
'''is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y'''
