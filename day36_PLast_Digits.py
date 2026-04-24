Last digits

if __name__ == "__main__":
    # 'last' stores the last three digits of the partial product of x to the power of y
    last = 1  
    print("Please enter two numbers x and y:")
    x = int(input("x = "))
    y = int(input("y = "))
    
    for i in range(1, y+1):
        # Multiply 'last' by 'x' and take modulo 1000 to keep only the last three digits
        last = last * x % 1000  
        
    print("The last three digits of %d raised to the power of %d are: %03d" %(x, y, last))
