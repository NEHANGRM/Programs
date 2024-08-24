l=[]
c=0
r=0
r2=0
sol=[]
for i in range(4):
    n=list(input().split(" "))
    t=int(n[0])
    t2=int(n[1])
    if(t!=0 and t2!=0):
        while(t!=0 and t2!=0):
            r=t%10
            r2=t2%10
            if((r+r2)>9):
                c+=1
            t=t//10
            t2=t2//10
        if(c==0):
            sol.append("No Carry operations")
        else:    
            sol.append(str(c)+" Carry operations")
        c=0
    else:
        sol.append("")
for i in sol:
    print(i)

            
    
        
