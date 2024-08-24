N=int(input())
l=[]
lt=[]
d=[]
dishes=[]
ing=[]
count=[]
ing2=[]
ing3=[]
items=0
c=0
k=0
m=0
dish=""
for i in range(N):
    l=input().split(",")
    lt.append(l)
s=input()
for i in lt:
    dishes.append(i[1])
    if(s in i):
        d.append(i[1])
print("Dishes for "+s+":",end=" ")
t=len(d)
for i in d:
    if(i==d[t-1]):
        print(i)
    else:
        print(i+",",end=" ")
for i in lt:
    ing=i[2].split(":")
    ing2.append(ing)
print("All ingredients:",end=" ")
t2=len(ing2)
for i in ing2:
    for j in i:
        ing3.append(j)
for i in ing2:
    for j in i:
        if(j==ing3[-1]):
            print(j)
        else:
            print(j+",",end=" ")
for i in ing2:
    for j in i:
        c+=1
    if(c>m):
        m=c
        dish=dishes[k]
        k+=1
    c=0
print("Dish with most ingredients:",dish)
    
    
    

