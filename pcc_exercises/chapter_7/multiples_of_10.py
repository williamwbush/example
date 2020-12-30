number = input("Enter a number. ")
number = int(number)

# Is the number a multiple of 10.
rem10 = number % 10
if rem10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")
