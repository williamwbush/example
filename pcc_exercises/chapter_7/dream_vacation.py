name_p = "What is your name? "
vacation_p = "Where would you like to go on vacation? "
repeat_p = "Would anyone else like to take this poll? "

responses = {}

poll_active = True

# Conduct poll.
while poll_active:
    print("\n")
    name = input(name_p)
    name = name.strip()
    vacation = input(vacation_p)
    vacation = (vacation.lower()).strip()
    responses[name] = vacation
   
    repeat = input(repeat_p)
    repeat.lower()
    if repeat == "no":
        poll_active = False 
    
# Print results of the poll.
print("\n")
for name, vacation in responses.items():
    print(name + " wants to go to " + vacation.title() + ".")
print("\n")

print(responses)
print("\n")


