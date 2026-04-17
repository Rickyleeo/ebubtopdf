if __name__ == '__main__':
    x = int(input("Please enter a 5-digit integer: "))
    if x < 10000 or x > 99999:
        print("Input error")
    else:
        ten_thousand = x // 10000       # Extract the ten-thousands digit (highest digit)
        thousand = x % 10000 // 1000    # Extract the thousands digit
        ten = x % 100 // 10             # Extract the tens digit
        indiv = x % 10                  # Extract the units digit
        if indiv == ten_thousand and ten == thousand:
            print("%d is a palindrome" %x)
        else:
            print("%d is not a palindrome" %x)
