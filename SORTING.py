#Works for only positive numbers.....
def bubble_sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if(a[j]>a[j+1]):
                (a[j],a[j+1])=(a[j+1],a[j])
    return(a)
def selection_sort(b):
    for i in range(len(b)-1):
        pos=i
        for j in range(i,len(b)):
            if(b[j]<b[pos]):
                    pos=j
        (b[i],b[pos])=(b[pos],b[i])
    return(b)
def insertion_sort(c):
     for i in range(1,len(c)):  # Iterate over the array starting from the second element
        key = c[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        c[j+1] = key
     return(c)

arr=list(map(int,input("Enter the elements to be sorted:").split(" ")))
ch=input("Enter your choice")
if(ch=="1"):
    bubarray=bubble_sort(arr)
    print("Sorted elements using bubble sort:",arr)
if(ch=="2"):
    selarray=selection_sort(arr)
    print("Sorted elements using Selection sort:")
    for i in selarray:
        print(i)
if(ch=="3"):
    insarray=insertion_sort(arr)
    print("Sorted elements using Insertion sort:")
    for i in insarray:
        print(i)
