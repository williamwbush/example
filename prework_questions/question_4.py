def is_leap_year(a_year):
    """Check if a given year is a leap year."""
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2600))
