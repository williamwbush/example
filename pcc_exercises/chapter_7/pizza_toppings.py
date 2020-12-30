prompt = "\nEnter a pizza topping:\n"
prompt += "Type 'quit' to exit.\n"

while True:
    message = input(prompt)

    if message == 'quit':
        print('Goodbye.')
        break
    else:
        print("We are adding " + message + " to your pizza.")