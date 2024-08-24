# Function to print a diamond pattern
def print_diamond(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

# Input the number of rows for the diamond
num_rows = int(input("Enter the number of rows for the diamond: "))

# Call the function to print the diamond pattern
print_diamond(num_rows)
