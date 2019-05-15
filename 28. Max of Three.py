def max(num1, num2, num3):
    if num1 - num2 >= 0:
        max = num1
        if max - num3 > 0:
           return max
        elif max - num3 < 0:
            max = num3
            return max
        else:
            return max
    elif num1 - num2 < 0:
        max = num2
        if max - num3 > 0:
            return max
        elif max - num3 < 0:
            max = num3
            return max
        else:
            return max

if __name__=='__main__':
    big = max(78, 1, 78)
    print(big)