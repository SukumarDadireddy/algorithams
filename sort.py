import time
#timing decorator
def timeit(func):
    def wrapper(a):
        start=time.time()
        result=func(a)
        stop=time.time()
        return stop-start
    return wrapper 




def mergesort(a):
    #base case,comparing 2 elements
    if len(a)==2:
        if a[0]>a[1]:
            return [a[1],a[0]]
        else:
            return [a[0],a[1]]
#dividing into sub problems
    if len(a)>2:
        fh=a[:(len(a)//2)]
        sh=a[(len(a)//2):]
    sfh=mergesort(fh)
    ssh=mergesort(sh)
   
    i=0
    j=0
    output=[]
    oi=0
#merging
 
    while i<len(sfh) and j<len(ssh):
        if sfh[i]<=ssh[j]:
            output.append(sfh[i])
            i=i+1
        else:
            output.append(ssh[j])
            j=j+1
        oi=oi+1
    if len(sfh)==i:
        output.extend(ssh[j:])
    else:
        output.extend(sfh[i:])

   
    return output
@timeit
def mergesort_time(a):
    r=mergesort(a)
    return r
        


a=mergesort_time([8,8,6,5,4,5,2,1])
print(a)
            
