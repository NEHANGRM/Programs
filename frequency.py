s=input()
st=list(s)
c=0
l=[]
r=0
ch=""
for k in st:
    if(k not in ch):
        ch=ch+k
for i in ch:
    for j in st:
        if(i==j):
            c+=1
    l.append(c)    
    c=0
    while(r<len(l)):
        print(str(i)+":"+str(l[r]))
        r+=1
               
        
