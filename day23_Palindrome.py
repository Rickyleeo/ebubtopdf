if __name__=="__main__":
    a = [0, 0, 0, 0, 0]  # List 'a' is used to store the five decomposed digits
    for i in range(95860, 100000):   # 'i' is the initial mileage; max is 100,000 as it remains a 5-digit number
        # Decompose the 5-digit number in 'i' from highest to lowest digit, 
        # and store them sequentially in array elements a[0] to a[4]
        t = 0  # Index for list 'a'
        k = 100000
        while k >= 10:
            a[t] = (i % k)//(k // 10)  # Store the decomposed digit
            k /= 10
            t += 1
        if a[0] == a[4] and a[1] == a[3]:
            print("The new symmetrical number on the odometer is: %d%d%d%d%d" %(a[0],a[1],a[2],a[3],a[4]))
            print("The speed of the car is: %.2f" %((i-95859)/2.0))
            break  # Exit the loop