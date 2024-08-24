N=int(input())
l=[]
lt2=[]
m=0
h=0
t=0
lt=[]
lt3=[]
for i in range(N):
    n=int(input())
    l.append(n)
ch=int(input())
if(ch>2):
    print("Error")
if(ch==1):
    for i in l:
        for j in l:
            if(i!=j):
                if(i%j==0):
                    lt.append(j)
    if(len(lt)==0):
       print("Null")
    else:
        for i in lt:
            print(i,end=" ")
if(ch==2):
    for i in l:
        for j in range (2,i+1):
            if(i%j==0):
                lt2.append(j)
    for i in lt2:
        if(lt2.count(i)>1):
            lt3.append(i)
    for i in set(lt3):
        print(i,end=" ")
        
            
    
            
