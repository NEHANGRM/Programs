def gcd(a,b):
    if(a>b):
        return(gcd(a-b,b))
    if(b>a):
        return(gcd(a,b-a))
    if(a==b):
        return(a)
n1=int(input())
n2=int(input())
c=gcd(n1,n2)
print(c)
