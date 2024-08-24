f=open("magic_numbers.txt","wt")
f.write("123456 234567 345678 456789 567890 678901 789012 890123 901234 123789")
f.close()
fo=open("magic_numbers.txt","rt")
rl=fo.readlines()
f.close()
l=rl[0].split()
print(l)
def compute_recursive_sum(l):
    if len(l)==0:
        return 0
    else:
        return int(l[0])+ compute_recursive_sum(l[1:])
c=0
def compute_power_sum(n):
    sn=str(n)
    global c
    c+=1
    if(n<=0):
        return(sn)
    else:
        return((int(sn[-1]))**(c-1))+int(compute_power_sum(n//10))

print("The sum of the magic numbers is:",compute_recursive_sum(l))
n=int(compute_recursive_sum(l))
print("The POWER sum of the magic numbers is:",compute_power_sum(n))
