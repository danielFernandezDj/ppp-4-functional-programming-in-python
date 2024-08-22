# Simple Example!
x = lambda a : a + 10
print(x(5))

print('----------------------------------')

# Unsorted list of tuples
subjects = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sort the list using a lambda function that sorts by the second element of each tuple
sorted_subjects = sorted(subjects, key=lambda x: x[1])

# Print the sorted list
print(sorted_subjects)

print('----------------------------------')

# Original list
numbers = [3, 6, 9, 2]

# Cube every element in the list using a lambda function
cubed_numbers = list(map(lambda x: x**3, numbers))

# Print the cubed list
print(cubed_numbers)

print('----------------------------------')

# Input list
numbers = [3, 6, 9, 2]

# Lambda function to check if a number is even (returns True) or odd (returns False)
is_even = lambda x: x % 2 == 0

# List comprehension to apply the lambda function to each element in the list
bool_list = [is_even(num) for num in numbers]

# Print the resulting list of booleans
print(bool_list)

print('----------------------------------')

# List comprehension to create a list of numbers from 1 to 100
numbers = [x for x in range(1, 101)]

# Print the resulting list
print(numbers)

print('----------------------------------')

# Input sentence
sentence = "The quick brown fox jumped over the fence."

# Dictionary comprehension to count the length of each word
word_lengths = {word: len(word) for word in sentence.split()}

# Print the resulting dictionary
print(word_lengths)
