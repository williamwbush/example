def is_consecutive(a_list):
    """Check if numbers in a list are consecutive."""
    #check for floats
    for num in a_list:
        if num % 1 != 0:
            return False
    #check if consecutive
    index = 0
    while index < len(a_list) - 1:
        if a_list[index+1] - a_list[index] != 1:
            return False
        else:
            index = index + 1
    return True
    
number_list = [1.5,2.5,3.5,4.5]
print(is_consecutive(number_list))


