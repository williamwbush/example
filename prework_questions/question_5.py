def is_consecutive(a_list):
    index = 0
    while index < len(a_list) - 1:
        if a_list[index+1] - a_list[index] != 1:
            return False
        else:
            index = index + 1
    return True
    
number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(is_consecutive(number_list))


