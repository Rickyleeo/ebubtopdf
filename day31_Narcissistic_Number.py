if __name__ == '__main__':
    print("result is: ")
    for n in range(100, 1000):  # Range of integers
        hun = n // 100  # Hundreds digit
        ten = (n - hun * 100) // 10  # Tens digit
        ind = n % 10  # Units digit
        m = hun*hun*hun + ten*ten*ten + ind*ind*ind # Sum of cubes
        if n == m:  # Check if the sum of the cubes equals the original number n
            print("%d \t" %n, end=" ")
