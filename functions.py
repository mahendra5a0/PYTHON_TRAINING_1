#FUNCTIONS'
#1.

'''name="laalu"
name1="valli"
name2="nikhi"
def greet(name):
    print(f"name of the student is {name}")
greet(name)
greet(name1) 
greet(name2)'''

#2.ADD TWO NUMBERS 

'''def add(num1,num2):
    sum1=num1+num2
    return sum1
a=34
b=35
c=add(a,b)
print(c)
'''

#PRODUCT OF TWO NUMBERS

'''def product(a,b):
    return a*b
print(product(23,2))'''

#CONVERT USD TO INR{1 USD= 83 INR}

'''def con(n):
    return n*83
print(con(4))
'''
#3.CALCULATE THE ARITHMETIC MEAN OF THE TWO NUMBERS   

'''def mean(num1,num2):
    mean1=(num1+num2)/2
    return mean1
a=23
b=33
c=mean(a,b)
print(c)'''

#4.MEAN OF N  NATURAL NUMBERS

'''n=int(input())
def mean(n):
    sum=(n*(n+1))/2
    mean1=sum/n
    return mean1
c=mean(n)
print(c)n'''

#5.FACTORIAL OF A NUMBER

'''def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
fac=factorial(5)
print(fac)'''

#sum of n natural numbers
'''def sumof(n):
    if n==0:
        return 0
    else:
        return n+sumof(n-1)
n=int(input("enter the number:"))
print(sumof(n))
'''
#factorial
'''def f(n):
    if n==0 or n==1:
        return 1
    else:
        return f(n-1)*n
n=5
print(f(n))'''
#fibanocii
'''def f(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
n=8
print(f(n))'''
#print 1 to n without loop
'''def f(n):
    if n>0:
        f(n-1)
        print(n)
n=10
f(n)

'''
#print n to 1 without loop
'''def f(n):
    if n>0:
        print(n)
        f(n-1)
n=10
f(n)'''

#sum of elements

'''def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n+f(n-1)
n=5
print(f(n))
    
'''
#avg of elements
'''print(f(n)/n)'''
#avg of elements in an array
'''def f(a,n):
    if n==1:
        return 1
    else:
       # return ((f(a,n-1)*(n-1))+a[n-1])/n
        return (f(a,n-1)+a[n-1])/n
a=[1,2,3,4,5]
n=len(a)
print(f(a,n))

'''
#convert decimal into binary


'''def f(n):
    if n==0:
        return 0
    else:
        return n%2+10*f(n//2)
n=17
print(f(n))'''  

#Print reverse of a string using recursion
'''def f(n):
    return n[::-1]
n=input("")
print(f(n))'''

#sum of digits

'''def f(n):
    if n==0:
        return 0
    else:
        return n%10+f(n//10)
n=12345
print(f(n))'''

#series

'''def fun(n):
    if n==0:
        return 
    fun(n-1)
    print(n)
    fun(n-1)
fun(10)'''

#fibanocii series

'''def f(n):
    if n==0 or n==1:
        return n
    return f(n-1)+f(n-2)
n1=10
if n1<=0:
    print("...")
else:
    for i in range(n1):
        print(i)

'''

#---------------------------------------------------------------------------------------
#Program to print multiplication table of a number

#iterative approach
'''n=int(input())
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
'''
#recursion approach
def fn(n,i):
    if i==11:
        return
    print(f"{n}*{i}={n*i}")
    i+=1
    fn(n,i)
fn(10,1)
