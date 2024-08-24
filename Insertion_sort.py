#Insertion sort for
n=int(input("Enter the size of the array:"))
arr=[]
for i in range(n):
    arr.append(int(input()))
print(arr)
for i in range(1,n):
    j=i
    while j>0 and arr[j]<arr[j-1]:
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j-=1
print(arr)

