prompt = "\nHow old are you?"
prompt += "\nTo exit this program, type 'quit'.\n"

#Exit the loop with 'break'.
while True: 
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("\nYour ticket is free.\n")
        elif age <= 12:
            print("\nYour ticket is $10.\n")
        else:
            print("\nYour ticket is $15.\n")

## Exit the loop with a conditional test.
# age = '0'
# while age != 'quit': 
#   age = input(prompt)
#    if age == 'quit':
#        continue
#    if int(age) < 3:
#        print("\nYour ticket is free.\n")
#   elif int(age) <= 12:
#        print("\nYour ticket is $10.\n")
#    else:
#        print("\nYour ticket is $15.\n")

## Exit the loop with an active variable (flag).
# active = True
# while active:
#    age = input(prompt)
#    if age == 'quit':
#        active = False
#    else:
#        if int(age) < 3:
#            print("\nYour ticket is free.\n")
#        elif int(age) <= 12:
#            print("\nYour ticket is $10.\n")
#        else:
#            print("\nYour ticket is $15.\n")