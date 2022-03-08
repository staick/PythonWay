def collatz(number):
    if number % 2 == 0:
        print(number)
        return number // 2
    elif number % 2 == 1:
        print(number)
        return number * 3 + 1

try:
    number = int(input("Enter number:"))
    while True:
        result = collatz(number)
        if result != 1:
            number = collatz(result)
        else:
            print(result)
            break
# 此处需要注意except的位置应在循环之后，否则输入的值不是整数，产生异常会导致number没有赋值，无法用于后续的循环中
except ValueError:
    print("Please enter an integer!")