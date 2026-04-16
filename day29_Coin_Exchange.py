if __name__=="__main__":
    # Variables x, y, and z represent the total value (in Jiao) 
    # of the exchanged 1-Yuan, 5-Jiao, and 1-Jiao coins respectively.
    count = 0  # Counter
    print("Possible exchange methods are as follows:")
    
    x = 0  # x is the value of 1-Yuan coins, possible values: {0,10,20,30,40,50}
    while x <= 50:
        y = 0  # y is the value of 5-Jiao coins, possible values: {0,5,10,15,20,25,30,35,40,45,50}
        while y <= 50 - x:
            z = 0  # z is the value of 1-Jiao coins, possible values: {0,1,...50}
            while z <= 50 - x - y:
                if x + y + z == 50:  # The total sum of x, y, and z must be 50
                    count += 1
                    if count % 3 == 0:   # Print one row every 3 columns
                        print(count, end="   ")
                        print("10*%d+5*%d+1*%d \t" % (x // 10, y // 5, z))
                    else:
                        print(count, end=" ")
                        print("10*%d+5*%d+1*%d \t" % (x // 10, y // 5, z), end=" ")
                z += 1
            y += 5
        x += 10
