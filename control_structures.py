#Conditional Statements
#1.IF statemnt
'''a = 33
b = 200
if b > a:
  print("b is greater than a") #b is greater than a'''

#2.Elif
'''a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #a and b are equal'''

#3.Else
'''a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") #a is greater than b'''
#One line if else statement, with 3 conditions:

'''a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #='''

#Examples
#1
'''a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") #Both conditions are True'''
#2
'''a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") #At least one of the conditions is True'''

#3.
'''a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")'''

#4.
'''x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")'''

#Looping Statements
#1.while
'''i = 1
while i < 6:
  print(i)
  i += 1
output:
1
2
3
4
5'''
#2.for
'''for x in "banana":
  print(x)
output:
b
a
n
a
n
a'''


#EXAMPLES

#1.SUM OF N NATURAL NUMBERS

'''n=int(input())
sum=(n*(n+1))//2
print(sum)'''

#2.PROGRAM TO COUNT THE NUMBER OF DIGITS IN AN INTEGER

'''n=int(input())
count=0
while n:
    d=n%10
    count+=1
    n=n//10
print(count)'''

#3.SUM OF ALL DIGITS

'''n=int(input())
count=0
while n:
    d=n%10
    count+=d
    n=n//10
print(count)
'''

#4.REVERSE THE GIVEN NUMBER

'''n=int(input())
rev=0
while n:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)'''

#5.PRODUCT OF DIGITS


'''n=int(input())
count=1
while n:
    d=n%10
    count=count*d
    n=n//10
print(count)'''  
#FACTORS OF A NUMBER
'''n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
'''
#6.SWAPPING TWO NUMBERS

'''a,b=5,7
a=a^b
b=a^b
a=a^b
print(a,b)

     
output:7 5'''
     


#-------------------------------------
#7..HCF OF TWO NUMBERS

'''n,m=map(int,input().split())
mine=min(n,m)
for i in range(1,mine):
    if n%i==0 and m%i==0:
        print(i)
        break
    
'''
#--------------------------------------




#----------------------------------------
#9.FACTORIAL OF A GIVEN NUMBER

'''n=int(input())    
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''


#------------------------------------------------

#FACTORS OF A NUMBER
'''n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
'''
#10. CALCULATE THE PRIME FACTORS OF A NUMBER

'''n=int(input())
prime=[]
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
 if count>2:
        print("not primw")
 else:'''
        
#---------------------------------------------        
#11.CHECK WHETHER THE NUMBER IS PRIME OR NOT

'''n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count>2:
    print("not prime")
else:
    print("prime")'''

'''n=int(input())
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
    print("prime")'''

'''n=int(input())
flag=0
for i in range(2,int((n**0.5)+1)):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("not prime")
else:
     print("prime")'''

#12.ARMSTRONG NUMBER
'''n=int(input())
m,b=n,n
count=0
val=0
while n:
    d=n%10
    count+=1
    n=n//10
while m:
    d1=m%10
    val=val+d1**count
    m=m//10
if b==val:
    print("armstrong")
else:
    print("not armstrong")'''
#13. number is a perfect square number or not
'''n=int(input()) 
d=n**0.5
if d**2==n:
    print("perfect")
else:
    print("not")
'''
#number ofprime numbers
'''n=int(input())
prm=0
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        prm+=1
print(prm)
    
'''
#2.Codeforces 466a
'''n,m,a,b=map(int,input("enter the value").split())
c1=a*n
print(c1)
c2=0
d=n//m
if n%m==0:
    c2=d*b
    print(c2)
else:
    c2=d*b+(n%m)*a
    print(c2)
if c1>c2:
    print("ticket is better")
else:
    print("pass is better")'''
#SUM OF ELEMENTS IN AN ARRAY
'''array=list(map(int,input().split()))
sum=0
for i in array:
    sum+=i
print(sum)
'''
#SUM OF ODD ELEMENTS IN AN ARRAY
'''array=list(map(int,input().split()))
sum=0
for i in array:
    if i%2!=0:
        sum+=i
print(sum)'''
#REVERSE AN ARRAY
'''array=list(map(int,input().split()))
print(array[::-1])

'''
#6.codeforces 617a
'''
n=int(input())
if n<5:
    print(1)
elif n%5==0:
    print(n//5)
else:
    print((n//5)+1)'''

#palindrome checker
'''
s=input("")
s1=s[::-1]
if s==s1:
    print("palindrome")
else:
    print("not")'''
