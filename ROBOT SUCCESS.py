ly=[]
lx=[]
x=0
y=0
lx.append(x)
ly.append(x)
sum=0
while(True):
    al=list(input().split())
    if 'U' in al:
        y=y+int(al[1])
        lx.append(x)
        ly.append(y)
    if 'D' in al:
        y=y-int(al[1])
        lx.append(x)
        ly.append(y)
    if 'L' in al:
        x=x-int(al[1])
        lx.append(x)
        ly.append(y)
    if 'R' in al:
        x=x+int(al[1])
        lx.append(x)
        ly.append(y)
    if not al:
        break
    sum+=int(al[1])
print(lx,end=' ')
print(ly)
print(sum)


