if __name__=="__main__":
    print("100000 Automorphic numbers ：")
    for number in range(0, 100000):
        mul = number
        k = 1
        # Determine the coefficient 'k' based on the number of digits in 'number'
        while (mul // 10) > 0:   
            mul //= 10
            k *= 10

        a = k * 10  # 'a' is the divisor used to intercept the last N digits of the product
        mul = 0     # Stores the last N digits of the calculated product
        b = 10      # 'b' is the coefficient used to extract specific digits of the multiplier
        while k > 0:
            # Formula: (Partial product + last N digits of multiplicand * M-th digit of multiplier) % a
            mul = (mul + (number % (k * 10)) * (number % b - number % (b // 10))) % a
            k //= 10  # Shift coefficient to process the next digit of the multiplicand
            b *= 10   # Move to the next digit of the multiplier
        
        # If the original number equals the last N digits of its square, it's an automorphic number
        if number == mul:  
            print("%ld " %number, end="\t")
