import heapq
from statistics import median

from attr import field
from scipy.fftpack import diff

file=open(r"/home/sukumar/Desktop/algorithams/Median.txt")

first_half=[]
second_half=[]
max_of_first_half=0
min_of_second_half=0
median_sum=0

for line in file:
   
    if (len(first_half)==0):
        heapq.heappush(first_half,-int(line))
        median_sum=median_sum-int(first_half[0])
        
    else:
        max_of_first_half=-first_half[0]
        if (max_of_first_half<=int(line)):
            heapq.heappush(second_half,int(line))
            
        else:
            
            heapq.heappush(first_half,-int(line))
        
        diffrence=len(first_half)-len(second_half)

        if(diffrence==2):
            heapq.heappush(second_half,-heapq.heappop(first_half))
            median_sum=median_sum-int(first_half[0])
          
        elif(diffrence==-2):
            heapq.heappush(first_half,-heapq.heappop(second_half))
            median_sum=median_sum-int(first_half[0])
            
        elif(diffrence==1):
            median_sum=median_sum-int(first_half[0])
            
        elif(diffrence==-1):
            median_sum=median_sum+int(second_half[0])
            
        elif(diffrence==0):
            median_sum=median_sum-int(first_half[0])



print(median_sum%10000)


        
         
            





        



    

    
        








    