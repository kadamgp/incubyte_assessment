def add_number_string(num_string):
    # for empty string
    if not num_string:
        return 0

    # for string with single number
    if(len(num_string)==1):
        return int(num_string)

    # when there are // then custom delimiter is used
    delimiter='\n'  # default delimiter is '\n'( for handling new lines )
    if(num_string.startswith("//")):
        two_parts=num_string.split("\n",1)  # spliting into two parts on first new line
        delimiter=two_parts[0][2:]
        num_string=two_parts[1]

    # replacing any delimiter with ','
    num_string=num_string.replace(delimiter,',')   

    # delimiter here is ','
    # for string with more than one number
 
    number_list = []
    for n in num_string.split(','):
        if n.strip() != '':          # ignoring empty strings (if there are multiple new lines then empty strings may occur)
            number_list.append(int(n))
            if int(n) < 0 :
                raise Exception("negative numbers not allowed <" + int(n) + ">")

    return sum(number_list)
    
