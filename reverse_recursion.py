def reverse(n,rev):
    if(n<=0):
        return(rev)
    else:
        return(reverse(n//10,rev*10+(n%10)))
num=int(input())
print(reverse(num,0))
