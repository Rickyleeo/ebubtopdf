if __name__=="__main__":
    # In 20 years, x1 is the number of 1-year terms, x2 is the number of 2-year terms, and so on.
    max = 0.0
    for x8 in range(0,3):
        t5 = (20-8*x8)//5   # Maximum number of 5-year deposits
        for x5 in range(0, t5+1):
            t3 = (20-8*x8-5*x5)//3  # Maximum number of 3-year deposits
            for x3 in range(0, t3+1):
                t2 = (20-8*x8-5*x5-3*x3)//2
                for x2 in range(0, t2+1):
                    x1 = 20-8*x8-5*x5-3*x3-2*x2    # Constraint for total deposit term
                    # Calculation logic
                    result = 2000* ((1+0.0063*12)**x1) * ((1+2*0.0066*12)**x2) * ((1+3*0.0069*12)**x3) * ((1+5*0.0075*12)**x5) * ((1+8*0.0084*12)**x8)
                    # y1, y2, y3, y5, y8 are used to record the deposit strategy with the highest return
                    if result > max:
                        max = result
                        y1 = x1
                        y2 = x2
                        y3 = x3
                        y5 = x5
                        y8 = x8
    # Output results
    print("The deposit strategy that yields the most interest is:");
    print("8-year term deposited %d times" %y8);
    print("5-year term deposited %d times" %y5);
    print("3-year term deposited %d times" %y3);
    print("2-year term deposited %d times" %y2);
    print("1-year term deposited %d times" %y1);
    print("Total principal and interest obtained by the depositor: %0.2f" %result);