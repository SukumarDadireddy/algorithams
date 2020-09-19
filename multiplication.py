
import time
#timing decorator
def timeit(func):
    def wrapper(*args):
        start=time.time()
        result=func(*args)
        stop=time.time()
        return  stop-start
    return wrapper 

# 3rd grade algo
@timeit
def brutemultiplication(a,b):
    l=[]
    z=0
    for i in str(b)[::-1]:

        sm=''
        c='0'
      
        for j in str(a)[::-1]:
            ssm=str((int(i)*int(j))+int(c))
           # print(ssm)
            #print(ssm)
            c='0'
            if len(ssm)>1:
                sm=sm+ssm[-1] 
                c=ssm[:-1:]
               # print(sm,c)
               # print(sm,c)
            else:
                sm=sm+ssm
       # print(c[-1::-1])
        sm=sm+c[-1::-1]
   
        sm=sm[-1::-1]+'0'*z

        z=z+1
        l.append(int(sm))
   # print(l)

    return sum(l)
    
    
#print(brutemultiplication(259,3))
#karatsuba multiplication
import random
@timeit
def karatsuba(x,y):
    if len(str(x))==1 or len(str(y))==1:
  
        return x*y
    if len(str(x))>len(str(y)):
        y=('0'*(len(str(x))-len(str(y))))+str(y)
    elif len(str(y))>len(str(x)):
        x=('0'*(len(str(y))-len(str(x))))+str(x)
    ol=len(str(x))

    mid=len(str(x))//2
    m=mid
    if len(str(x))%2 !=0:
        mid=mid+1

    a=int(str(x)[:mid])
    b=int(str(x)[mid:])
    c=int(str(y)[:mid])
    d=int(str(y)[mid:])
  
    one=karatsuba(a,c)
    three=karatsuba((a+b),(c+d))
    two=karatsuba(b,d)
    four=three-two-one



    return (one*(10**(m*2)))+(four*(10**m))+two

print(karatsuba(123,13))
print(brutemultiplication(123,13))

# random inputs
inputs=[]
import random
min=1
max=9
for i in range(25):
    min=int(str(min)+('0'*i))
    max=int(str(max)+('9'*i))
    inputs.append((random.randint(min,max),random.randint(min,max)))
#getting outputs for random inputs ranging length from 1 to 26 digits
bmt=[]
kmt=[]
for i in inputs:
    bmt.append(brutemultiplication(i[0],i[1]))
    kmt.append(karatsuba(i[0],i[1]))
#graphing
import matplotlib.pyplot as plt
plt.plot([i for i in range(1,26)],bmt,'b')#blue graph for 3rd grade algo
plt.plot([i for i in range(1,26)],kmt,'r')#red for karatsuba algo
plt.show()
    

