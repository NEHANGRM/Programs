string=input()
s=""
lt=[]
for i in range(len(string)):
    for k in range(i,len(string)):
        for j in range(k,len(string)):
                s+=string[j]
                lt.append(s)
        s=""
        break
print(lt)
