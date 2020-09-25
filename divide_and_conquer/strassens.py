import numpy as np
def strassen(a,b):
    x=np.array(a)
    y=np.array(b)
    l,b=x.shape
    ll,bb=y.shape
    #base case
    if l==1 and b==1:
        return x*y
    #divide
    if l>1 or b>1:
        midr=l//2
        midc=b//2
        midsr=ll//2
        midsc=bb//2
        a=x[0:midr,0:midc]
        b=x[0:midr,midc:]
        c=x[midr:,:midc]
        d=x[midr:,midc:]
        e=y[0:midsr,0:midsc]
        f=y[0:midsr,midsc:]
        g=y[midsr:,:midsc]
        h=y[midsr:,midsc:]

    
    p1=strassen(a,(f-h))
    p2=strassen((a+b),h)
    p3=strassen((c+d),e)
    p4=strassen(d,(g-e))
    p5=strassen((a+d),(e+h))
    p6=strassen((b-d),(g+h))
    p7=strassen((a-c),(e+f))
    
    ft=p5+p4-p2+p6
    st=p1+p2
    fd=p3+p4
    sd=p1+p5-p3-p7
    
    top=np.concatenate((ft,st),axis=1)
    down=np.concatenate((fd,sd),axis=1)
 
    return np.concatenate((top,down))


if __name__=="__main__":
    print(strassen(np.arange(1,17).reshape(4,4),np.arange(1,17).reshape(4,4)))
   