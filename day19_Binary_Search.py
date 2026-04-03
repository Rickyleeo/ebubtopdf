if __name__ == "__main__":
    a = [-3, 4, 7, 9, 13, 45, 67, 89, 100, 180]
    low = 0  # Lower bound of the array
    high = len(a) - 1  # Upper bound of the array
    k = -1  # Variable to store the index
    print("Data in array a:")
    for i in a:
        print(i, end=" ")  # Output the original data sequence in the array
    print()
    m = int(input("Enter m = : "))  # Variable m is the integer to be searched
    while low <= high:  # Control condition to continue searching
        mid = (low + high) // 2 # Variable mid is the middle position of the array sequence
        if m < a[mid]:
            high = mid - 1
        else:
            if m > a[mid]:
                low = mid + 1
            else:
                k = mid
                break   # Exit the loop once the element is found
    if k >= 0:
        print("m = %d, index = %d" %(m, k))
    else:
        print("Not be found!")
