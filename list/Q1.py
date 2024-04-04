def find_largest(numbers):
   
    #Finds the largest number from a list of numbers.
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def find_smallest(numbers):
    
    #Finds the smallest number from a list of numbers.
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

# Main program to test the functions
numbers = input("Input array: ").split()
numbers = [int(num) for num in numbers]
print("a=", numbers)
print("Largest number=", find_largest(numbers))
print("Smallest number=", find_smallest(numbers))
