
import time
def timeit(func):
    def wrapper(*args):
        start=time.time()
        result=func(*args)
        stop=time.time()
        return result, stop-start
    return wrapper 


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
    
    
print(brutemultiplication(259,3))
import random

