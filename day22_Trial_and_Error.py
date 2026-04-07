if __name__=="__main__":
    flag = 0   # flag acts as a control flag
    i = 23
    while flag == 0:
        j = 1   # j represents the number of sales (iterations)
        x = i   # x represents the number of fish remaining at each step
        while j <= 4 and x >= 11:
            if (x + 1) % (j + 1) == 0:   # Check if (x + 1) is divisible by (j + 1)
                x -= (x+1)//(j+1)
            else:
                x = 0
                break
            j += 1
        if j == 5 and x == 11:
            print("There were originally %d goldfish in the tank." %i)
            flag = 1   # Result found, set flag to 1 to exit the search
        i += 2