favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
new_poll_takers = ('jen', 'sarah', 'jon', 'robert')
for respondent in new_poll_takers:
    if respondent in favorite_languages:
        print(respondent.title() + ', thank you for responding.')
    else:
        print(respondent.title() + ", please take the poll.")
