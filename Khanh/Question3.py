def remove_empty_strings(strings):
    return list(filter(None, strings))

def find_substring_occurrences():
    string = input("String Input str1: ")
    substring = input("String Input str2: ")
    count = string.lower().count(substring.lower())
    print("Expected Outcome: The '",substring, "' count is:" , count)

def split_string():
    string = input("String Input: ")
    parts = string.split("-")
    print("Displaying each substring: ", parts)

def replace_special_characters():
    string = input("String Input: ")
    for char in "!@#$%^&*()_+-=[]{}|\\;:'\",./<>?":
        string = string.replace(char, "#")
    print("Expected Output:", string)

def count_characters():
    string = input("String Input: ")
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print("Expected Output:")
    for char, count in char_count.items():
        print(char, count)

while True:
    print("\nSelect task")
    print("1. Remove empty strings from a list of strings")
    print("2. Find all occurrences of a substring in a given string by ignoring the case")
    print("3. Split a string on hyphens (“-“)")
    print("4. Replace each special symbol with # in the following string")
    print("5. Count occurrences of all characters within a string")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        strings = input("Count occurrences of all characters within a string (,) ")
        string_list = strings.split(",")
        non_empty_strings = remove_empty_strings(string_list)
        print("After removing empty strings: ", non_empty_strings)
    elif choice == 2:
        find_substring_occurrences()
    elif choice == 3:
        split_string()
    elif choice == 4:
        replace_special_characters()
    elif choice == 5:
        count_characters()
    elif choice == 0:
        break
    else:
        print("Invalid selection. Please choose again!")
