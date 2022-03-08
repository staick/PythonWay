def collatz(number):
    if number % 2 == 0:
        print(number)
        return number // 2
    elif number % 2 == 1:
        print(number)
        return number * 3 + 1

number = int(input("Enter number:"))
while True:
    result = collatz(number)
    if result != 1:
        number = collatz(result)
    else:
        print(result)
        break