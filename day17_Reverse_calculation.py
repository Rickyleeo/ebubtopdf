if __name__ == "__main__":
    i = 0
    money = 0.0
    while i < 5:
        # Reverse calculation: Assume an annual deposit of 1000, discounted at a monthly interest rate of 0.63%.
        money = (money + 1000) / (1 + 0.0063 * 12)
        i += 1
    print("Amount to be deposited: %0.2f" % money)   # Result rounded to 2 decimal places
