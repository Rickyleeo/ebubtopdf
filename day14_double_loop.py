if __name__ == "__main__":
    # cock: roosters, hen: hens, chicken: chicks. Total must be 100 birds.
    
    # Outer loop controls the number of roosters (max 20, since 5 * 20 = 100)
    cock = 0
    while cock <= 20:
        # Middle loop controls the number of hens (max 33, since 3 * 33 = 99)
        hen = 0
        while hen <= 33:
            # The number of chicks is determined by the remaining count
            chicken = 100 - cock - hen
            
            # Check if the total price is exactly 100
            # Roosters: 5 each, Hens: 3 each, Chicks: 3 for 1 (1/3 each)
            if (5 * cock + 3 * hen + chicken / 3.0 == 100):
                print(f"cock = {cock:2d}, hen = {hen:2d}, chicken = {chicken:2d}")
                
            hen += 1
        cock += 1