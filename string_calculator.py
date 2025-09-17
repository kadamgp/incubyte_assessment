def add_number_string(num_string):
    # for empty string
    if not num_string:
        return 0

    # for string with single number
    if(len(num_string)==1):
        return int(num_string)

    # delimiter here is ','
    # for string with more than one number
    number_list=list(map(int,num_string.split(',')))
    return sum(number_list)
    
