c=0
def power_sum(n):
    global c
    c+=1
    if(n==0):
        return(0)
    else:
        return((n%10)**(c-1)+power_sum(n//10))
num=int(input())
a=power_sum(num)
print(a)
