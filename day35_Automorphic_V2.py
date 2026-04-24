for number in range(0, 100000):
    n = len(str(number))
    if (number**2) % (10**n) == number:
        print(number, end="\t")
s