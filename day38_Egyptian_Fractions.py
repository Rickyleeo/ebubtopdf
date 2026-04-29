if __name__ == "__main__":
    print("Please enter a fraction：", end=" ")
    a, b = [int(i) for i in input().split()]
    print("The entered score is：%ld/%ld" %(a, b))
    print("Egyptian fraction：", end=" ")
    while 1:
        # If the numerator doesn't divide the denominator, 
        # extract an Egyptian fraction with denominator b//a + 1
        if b % a != 0:  
            c = b // a + 1
        else:
            c = b // a
            a = 1
        if a == 1:
            print("1/%ld\n" %c, end="")
            break
        else:
            print("1/%ld + " %c, end="")
        
        a = a * c - b   # Calculate the numerator of the remainder
        b = b * c       # Calculate the denominator of the remainder
        
        # If the remainder's numerator is 3 and the denominator is even, 
        # output the last two Egyptian fractions
        if a == 3 and b % 2 == 0:  
            print("1/%ld + 1/%ld\n" %(b//2, b))
            break
