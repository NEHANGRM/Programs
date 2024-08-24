import sys
n=int(input())
d={}
c=0
count=0
s=0
avg=0
t=0
for i in range (n):
    r=int(input())
    gpa=float(input())
    d[r]=gpa
while (True):
    ch=int(input())
    if(ch==1):
        print(d)
    if(ch==2):
        for i in d.keys():
            if(d[i]>7):
                c+=1
        print(c)
    if(ch==3):
        for i in d.keys():
            if(d[i]<7):
                count+=1
                s+=d[i]
        avg=s/count
        print(avg)
    if ch==4:
        for i in d:
            if d[i]<7:
                min=d[i]
                print("Minimum value",min)
                break
        for i in d:
            if d[i]<7:
                if abs(d[i]-7)<abs(min-7):
                    min=d[i]
        for i in d:
            if d[i]==min:
                print(i)
    if ch==5:
        a=max(d.values())
        for i in d:
            if d[i]==a:
                print(i)
    if(ch>5):
        exit()
    

