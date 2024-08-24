lt=[]
l=[]
f=[]
fnew=[]
N=int(input())
for i in range(N):
    n=int(input())
    lt.append(n)
    l=list(set(lt))
ch=int(input())
if(ch==1):
    n1=int(input())
    if(n1 in l):
        for j in range(1,n1+1):
            if(n1%j==0):
                f.append(j)
    else:
        print("Error")
    for i in f:
            print(i,end=" ")       
    
if(ch==2):
    for i in l:
        for j in range(1,i+1):
            if(i%j==0):
                f.append(j)
        print(f)
    for i in range(len(f)):
        for j in range(i):
            try:
                if(f[i]==f[j]):
                    f.remove(f[i])
            except IndexError:
                break
    for i in f:
        print(i,end=" ")
        
        
