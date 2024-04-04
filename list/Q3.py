def reverse_list():
    user_input = input("Input list: ")
    lst = user_input.split(",")
    lst.reverse()
    return lst

# Example usage
reversed_list = reverse_list()
print(reversed_list)

def remove_duplicates():
    user_input = input("Input list: ")
    lst = user_input.split(",")
    unique_lst = list(set(lst))
    return unique_lst

# Example usage
unique_list = remove_duplicates()
print(unique_list)


def remove_common_elements():
    list1_input = input("Input list 1: ")
    list2_input = input("Input list 2: ")
    list1 = list1_input.split(",")
    list2 = list2_input.split(",")
    for element in list1:
        if element in list2:
            list2.remove(element)
    return list2

# Example usage
result_list = remove_common_elements()
print(result_list)
