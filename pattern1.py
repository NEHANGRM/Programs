''' 
     1 
    1 1  
   1 2 1   
  1 3 3 1    
 1 4 6 4 1 
 '''

n=int(input())
t=1
st=""
for i in range(1,n+1):
    s=t
    for j in range(1,n+1):
        st=st+" "
        if(i+j>=n+1):
            while(s>0):
                r=int(s%10)
               
                st=st+str(r)+" "
                s=int(s/10)

    print(st)            
    st=""            
    t=t*11
    
