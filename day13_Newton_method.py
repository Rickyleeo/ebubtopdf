# Function to find the root of an equation using Newton's method
def solution(a, b, c, d):
    x = 1.5
    x0 = x  # Use the newly calculated x to replace the previous x0
    # f represents the value of the equation, fd represents the derivative
    f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
    fd = 3 * a * x0 * x0 + 2 * b * x0 + c
    h = f / fd
    x = x0 - h  # Calculate a value of x closer to the actual root
    while abs(x - x0) >= 1e-5:
        x0 = x
        f = a * x0 * x0 * x0 + b * x0 * x0 + c * x0 + d
        fd = 3 * a * x0 * x0 + 2 * b * x0 + c
        h = f / fd
        x = x0 - h  # Calculate a value of x closer to the actual root

    return x


if __name__ == '__main__':
    print("Please enter four valid numbers：")
    # a, b, c, d represent the coefficients of the equation
    a, b, c, d = map(float, input().split())
    print("Please enter the coefficients：" , a, b, c, d)
    # x stores the calculated root of the equation
    x = solution(a, b, c, d)
    print("Parameters x=%.6f"% x)