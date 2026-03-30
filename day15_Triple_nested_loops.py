if __name__=="__main__":
    # Three children A, B, and C borrowing from 5 books; each person borrows one book at a time.
    # a, b, and c represent the book IDs chosen by A, B, and C respectively.
    i = 0  # i tracks the number of valid borrowing combinations
    print("Book IDs chosen by A, B, and C:")

    # Nested loops to simulate book selection for each child
    for a in range(1, 6):      # Controls book ID for child A
        for b in range(1, 6):  # Controls book ID for child B
            for c in range(1, 6): # Controls book ID for child C
                # Ensure all three children pick different books
                if a != b and a != c and c != b:
                    print("A:%2d  B:%2d  C:%2d    " %(a, b, c) ,  end='')
                    i += 1
                    # Wrap to a new line every 4 combinations for better formatting
                    if i % 4 == 0:
                        print()  
                        
    print("Total number of valid borrowing methods: %d" %i)