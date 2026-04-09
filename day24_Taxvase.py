TAXBASE = 2000

# Divided into 9 brackets. Each bracket contains: (start_point, end_point, tax_rate)
TaxTable = [(0, 500, 0.05),
            (500, 2000, 0.10),
            (2000, 5000, 0.15),
            (5000, 20000, 0.20),
            (20000, 40000, 0.25),
            (40000, 60000, 0.30),
            (60000, 80000, 0.35),s
            (80000, 100000, 0.40),
            (100000, 1e10, 0.45)]

# Calculate tax
def CaculateTax(profit):
    tax = 0.0
    profit_to_tax = profit - TAXBASE  # Income exceeding the tax threshold
    
    if profit_to_tax <= 0:
        return 0.0

    for start, end, rate in TaxTable:
        # Check if the profit falls within the current tax bracket
        if profit_to_tax > start:
            # Calculate the amount of profit that belongs to this bracket
            current_bracket_profit = min(profit_to_tax, end) - start
            current_tax = current_bracket_profit * rate
            tax += current_tax
            
            # Show the calculation for each step
            remaining = max(0, profit_to_tax - end)
            print("Tax Range: %6d~%10d  Tax in this range: %8.2f  Remaining: %8d" 
                  % (start, end, current_tax, remaining))
            
            if profit_to_tax <= end:
                break
                
    return tax

if __name__ == '__main__':
    try:
        income = float(input("Please enter your personal income: "))
        tax = CaculateTax(income)
        print("-" * 30)
        print("Your personal income tax is: %12.2f" % tax)
    except ValueError:
        print("Please enter a valid number.")
