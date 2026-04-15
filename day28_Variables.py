if __name__=="__main__":
    # Variables x, y, and z represent men, women, and children respectively
    print("    Men  Women  Children ")
    number = 0   # Counter for the number of possible solutions
    x = 0   # The range for men is [0-10]
    while x <= 10:
        y = 20 - 2 * x   # y can be determined once x is fixed
        z = 30 - x - y   # z can be determined once x and y are fixed
        if 3 * x + 2 * y + z == 50:
            number += 1
            print("%2d:%4d%5d%6d"  %(number, x, y, z))
        x += 1

