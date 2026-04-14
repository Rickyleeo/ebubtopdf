if __name__=="__main__":
    # Use a loop to calculate the cumulative sum
    i = 1
    sum = 0.0
    while i <= 64:
        sum = sum + 2**(i-1)
        # print("sum" , i , "=" , sum)
        i += 1
    # Total grains of wheat the King needs to give the Chancellor:
    print("Total grains of wheat the King needs to give the Chancellor：\n%f\n" %sum)   # Print the result
