import datetime

def get_fish_status(target_year, target_month, target_day):
    """Calculate and return the status of 'fishing' or 'sun-drying the net'"""
    try:
        # Define the starting reference date
        start_date = datetime.date(1990, 1, 1)
        end_date = datetime.date(target_year, target_month, target_day)
        
        # Calculate total days (including the current day, hence +1)
        delta = (end_date - start_date).days + 1
        
        if delta < 1:
            return "The date is too early; fishing hadn't started yet!"

        # Logic: 5-day cycle. Days 1, 2, 3 = Fishing; Days 4, 0 (5) = Sun-drying
        cycle_day = delta % 5
        status = "Fishing 🐟" if 1 <= cycle_day <= 3 else "Sun-drying Net ☀️"
        
        return f"Day {delta} since 1990-01-01. Today's task: {status}"
    
    except ValueError:
        return "⚠️ Invalid date! Please check for errors like 'Feb 30th'."

def main():
    print("=== Fisherman's Schedule Query System ===")
    print("(Enter 'q' to exit the program)\n")
    
    while True:
        user_input = input("Enter date (e.g., 2023 5 20): ").strip()
        
        # Exit condition
        if user_input.lower() == 'q':
            print("Closing the system. Goodbye!")
            break
            
        try:
            # Parse the input by splitting whitespace and mapping to integers
            y, m, d = map(int, user_input.split())
            print(get_fish_status(y, m, d))
        except ValueError:
            print("Please enter three numbers (Year Month Day) separated by spaces.")
        print("-" * 40)

if __name__ == "__main__":
    main()
