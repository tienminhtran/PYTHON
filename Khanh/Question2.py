def count_characters():
    s = input("Input String: ")
    num_letters = 0
    num_digits = 0
    num_special = 0
    
    for char in s:
        if char.isalpha():
            num_letters += 1
        elif char.isdigit():
            num_digits += 1
        elif char.isspace():
            pass
        else:
            num_special += 1
            
    print("Chars = ", num_letters)
    print("Digits = ", num_digits)
    print("Symbol = ", num_special)
count_characters()
