
if __name__ == "__main__":
    # i represents the first two digits, j represents the last two digits, k is the license plate number
    # i 代表前两位数字，j 代表后两位数字，k 代表车牌号
    flag = 0  # Loop control flag; exit all loops when set to 1
              # 循环标识变量，为 1 时退出所有循环
              
    for i in range(10):
        if flag:
            break
        for j in range(10):  # Exhaustively test combinations of front and back digit pairs
                             # 穷举前两位和后两位车牌数字
            if flag:
                break
            
            # Check if the first two digits are different from the last two
            # 判断前两位和后两位数字是否相同（aabb 形式要求 i != j）
            if i != j:
                # Construct the 4-digit license plate number (e.g., 7744)
                # 组成 4 位车牌号码
                k = 1000 * i + 100 * i + 10 * j + j
                
                # Check if k is a perfect square; if so, output the result
                # 判断 k 是否是某个数的平方，是就输出
                for temp in range(31, 100):
                    if temp * temp == k:
                        print("License plate number is: ", k)
                        flag = 1
                        break
