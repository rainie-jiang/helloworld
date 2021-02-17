

def find_max(list):
    max_list=list[0]
    for list2 in list:
        if list2 > max_list:
            max_list=list2
    return max_list