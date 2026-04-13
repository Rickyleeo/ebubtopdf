def computing_ladder(n):
    print("The ladder numbers between 1-%d are:" %n)
    count = 0
    for i in range(7, n+1):
        # Conditions that the ladder number must satisfy
        if (i % 7 == 0) and (i % 6 == 5) and (i % 5 == 4) and (i % 3 == 2):
            count += 1   # count tracks the number of integers between 1-n that meet the criteria
            print("%d" %i)
    print("Between 1-%d, there are %d numbers that meet Einstein's ladder requirements." %(n, count))

if __name__=="__main__":
    while True:
        try:
            n = int(input("Please enter the value of n: "))
            computing_ladder(n) # Fixed: removed the extra 'sum' argument
        except ValueError:
            print("Please enter a valid integer.")
            break