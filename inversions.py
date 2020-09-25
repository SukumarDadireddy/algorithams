def inversions(a):
    fh=[]
    sh=[]
    #base case,comparing 2 elements
    if len(a)==1:
        return a,0
#dividing into sub problems
    if len(a)>1:
        fh.extend(a[:(len(a)//2)])
        sh.extend(a[(len(a)//2):])
    sfh,fni=inversions(fh)
    ssh,sni=inversions(sh)
   
    i=0
    j=0
    output=[]
 
#merging
    no_of_inv=fni+sni
    while i<len(sfh) and j<len(ssh):
        if sfh[i]<=ssh[j]:
            output.append(sfh[i])
            i=i+1
        else:
            output.append(ssh[j])
            j=j+1
            no_of_inv=no_of_inv+(len(sfh)-i)
    if len(sfh)==i:
        output.extend(ssh[j:])
    else:
        output.extend(sfh[i:])

   
    return output,no_of_inv

print(inversions([6,5,4,3,2,1]))
