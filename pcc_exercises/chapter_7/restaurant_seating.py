prompt = "How many people are in the dinner group? "
group = input(prompt)
group = int(group)
if group > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")