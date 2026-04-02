def bubbleSort(a):
    # Get the total length of the list to prepare for subsequent comparisons
    n = len(a)
    # Perform n-1 rounds of comparison to control the number of passes
    for i in range(1, n):
        # Control the number of comparisons within each round
        for j in range(0, n-i):
            # Swap elements
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
    # Print the list after sorting
    for a1 in a:
        print(a1, end=" ")


if __name__=="__main__":
    print("Please enter initial values for the list, no trailing spaces:")
    x = input()
    a = x.split(" ")  # Split elements by space
    for i in range(0, len(a)):  # Handle multiple inputs
        a[i] = int(a[i])
    print("The list elements you entered are:\n", a)
    print("The array elements after swapping are:")
    bubbleSort(a)
