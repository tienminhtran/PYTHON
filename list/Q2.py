def print_strings(strings):
    for string in strings:
        if len(string) >= 3 and string[0] == string[-1]:
            print(string)

def find_common_items(list1, list2):

    common_items = []
    for item in list1:
        if item in list2 and item not in common_items:
            common_items.append(item)
    return common_items

# Main program to test the functions
string_input = input("Input alist: ")
strings = string_input.split()
print("Expected: ")
print_strings(strings)

list1_input = input("list1=")
list1 = list1_input.split()
list2_input = input("list2=")
list2 = list2_input.split()
common_items = find_common_items(list1, list2)
print("Common=", common_items)
