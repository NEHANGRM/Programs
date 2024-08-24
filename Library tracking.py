l=[]
lt=[]
book=[]
l2=[]
lt2=[]
k=0
c=0
r=[]
m=0
temp=0
n2=[]
M=int(input())
for i in range(M):
    l=input().split(",")
    lt.append(l)
B=int(input())
for i in range(B):
    l2=input().split(",")
    lt2.append(l)
    n=l2[1].split(":")
    n2.append(n)
s=input().split(",")
print("Books in"+s[0]+":",end=" ")
for i in lt:
    for j in i:
        if(s[0]==j):
            book.append(i[1])
for i in book:
    if(i==book[len(book)-1]):
        print(i)
    else:
        print(i+",",end=" ")
for i in n2:
    for j in i:
        r.append(j)
for i in range(len(r)-1):
    for j in range(len(r)):
        if(r[i]==r[j]):
            c+=1
    temp=lt[k]
    if(k<M):
        k+=1
    if(c>m):
        m=c
        aut=temp[2]
print("Most Popular Author:",aut)
        
                    

    
        

            
            
