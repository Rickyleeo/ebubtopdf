if __name__ == "__main__":
    count = 0   # counter
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != k and i != j and j != k:   # check if the three digits are unique
                    count += 1
                    print("%d%d%d  " %(i,j,k), end=" ")
                    if count % 8 == 0:
                        print()
    print("Total number of unique 3-digit numbers: %d" %count)
