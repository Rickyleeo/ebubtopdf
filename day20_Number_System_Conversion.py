# Convert character to number
def char_to_num(ch):
    if ch >= '0' and ch <= '9':
        return int(ch)  # Convert numeric character to integer
    else:
        return ord(ch)  # Convert letter character to its ASCII/numeric value


# Convert number to character
def num_to_char(num):
    if num >= 0 and num <= 9:
        return str(num)  # Convert digits 0-9 to string
    else:
        return chr(num)  # Convert values >= 10 to their character representation


# Convert other number systems to decimal
def source_to_decimal(temp, source):
    decimal_num = 0  # Store the accumulated sum

    for i in range(len(temp)):  # Accumulate values
        decimal_num = (decimal_num * source) + char_to_num(temp[i])

    return decimal_num


# Convert decimal to other number systems
def decimal_to_object(decimal_num, object):
    decimal = []
    while decimal_num:
        decimal.append(num_to_char(decimal_num % object)) # Get remainder and convert to character
        decimal_num //= object  # Divide decimal number by base

    return decimal


# Output the converted result (reverse the remainder list)
def output(decimal):
    f = len(decimal)-1
    while f >= 0:
        print(decimal[f], end='')
        f -= 1
    print()

if __name__ == '__main__':
    MAXCHAR = 101  # Maximum allowed string length
    flag = 1  # Flag to control program exit
    while flag:  # Use flag to control loop execution
        print("Enter the number: ", end='')
        temp = input()
        print("Enter the source base: ", end='')
        source = int(input())
        print("Enter the target base: ", end='')
        object = int(input())
        print("Converted result: ", end='')
        decimal_num = source_to_decimal(temp, source)
        decimal = decimal_to_object(decimal_num, object)
        output(decimal)
        print("Enter 1 to continue, 0 to exit: ")
        flag = int(input())
