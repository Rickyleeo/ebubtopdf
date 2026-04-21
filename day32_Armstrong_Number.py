if __name__ == "__main__":
    a = [0, 0, 0]  # List 'a' stores the ones, tens, and hundreds digits
    print("Armstrong numbers up to 1000:")
    for i in range(2, 1000):
        t = 0
        k = i
        # Split the number from the lowest to the highest digit
        while k:
            a[t] = k % 10
            k = k // 10
            t += 1
        sum = a[0]**3 + a[1]**3 + a[2]**3
        if i == sum:
            print("%d \t " %i, end=" ")
