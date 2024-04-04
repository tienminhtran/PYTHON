with open('file1.txt', 'r') as file1:
    with open('file2.txt', 'w') as file2:
        word_count = 0
        for line in file1:
            file2.write(line)
            word_count += len(line.split())
        print("Expected:", word_count)
