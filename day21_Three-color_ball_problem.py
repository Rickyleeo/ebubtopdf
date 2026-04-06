if __name__=="__main__":
    # Randomly pick 8 balls out of 12: m red balls, n white balls, and 8-m-n black balls.
    # The range of m is [0,3], and the range of n is also [0,3]. 
    # The number of black balls must be 6 or fewer, i.e., 8-m-n ≤ 6.
    print("\t Red \t White \t Black")
    print("........................")
    num = 0
    for m in range(0, 4):
        for n in range(0, 4):
            if 8-m-n <= 6:
                num += 1
                print("%2d:  %d \t\t %d \t\t %d" %(num, m, n, 8-m-n))
