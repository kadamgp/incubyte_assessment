def add_number_string(num_string):
    # for empty string
    if not num_string:
        return 0

    # for string with single number
    if(len(num_string)==1):
        return int(num_string)

    # handling new line between the number string
    num_string=num_string.replace('\n',',')

    # delimiter here is ','
    # for string with more than one number
 
    number_list = []
    for n in num_string.split(','):
        if n.strip() != '':          # ignoring empty strings (if there are multiple new lines then empty strings may occur)
            number_list.append(int(n))

    return sum(number_list)
    
