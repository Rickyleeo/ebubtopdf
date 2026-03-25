if __name__=="__main__":
    fib1 = 1
    fib2 = 1
    i = 1
    while i <= 15:  #Calculate two numbers per iteration, so loop up to 15
        print("%8d    %8d" %(fib1, fib2), end="      ")
        if i % 2 == 0:
            print()
        fib1 = fib1 + fib2  # Rabbit count for the latest month
        fib2 = fib1 + fib2  # Rabbit count for the following month
        i += 1
