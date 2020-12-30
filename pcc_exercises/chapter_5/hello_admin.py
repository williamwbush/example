usernames = ['tiger1', 'tiger2', 'tiger3', 'tiger4', 'admin']
if usernames:
    for username in usernames:
        if username == "admin":
            print("Welcome, admin. Aren't you special.")  
        else:
            print('Welcome, ' + username + ", thank you for loggin in.")
else:
    print('We need to find some users.')


