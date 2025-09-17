def add_number_string(num_string):
    if(len(num_string)==0):
        return 0
    if(len(num_string)==1):
        return int(num_string)
        
    number_list=num_string.split(',')
    return int(number_list[0]) + int(number_list[1])
    
