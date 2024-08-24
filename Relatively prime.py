def prime_1(n1,n2):
    c=0
    for i in range (2,(n1+n2)):
        if(n1%i==0 and n2%i==0):
                  c+=1
    if(c==0):
        return True
    else:
        return False
    
num1=int(input())
num2=int(input())
if(prime_1(num1,num2)):
    print("Relatively Prime",num1,num2)
else:
    print("NOT")
            
