current_users = ['tiger1', 'tiger2', 'tiger3', 'tiger4', 'admin']
new_users = ['tiger5', 'tiger6', 'tiger7', 'Tiger4', 'admin']
for user in new_users:
    if user.lower() in current_users:
        print('That username is already in use.')
    else:
        print('That username is available.')
    