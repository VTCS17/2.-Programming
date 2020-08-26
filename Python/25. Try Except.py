
try:
    num = int(input("Enter a number: "))
    print(num)
    value = 10 / 0
except ZeroDivisionError as err:
    print(err)
except ValueError as A:
    print(A)