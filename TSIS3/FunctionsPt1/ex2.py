def grams_to_ounces(grams):
    return grams / 28.3495231

# Example usage
print(grams_to_ounces(100))  # Convert 100 grams to ounces


def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# Example usage
print(fahrenheit_to_celsius(98.6))  # Convert 98.6°F to °C


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 11, 13, 17]))  # Filter prime numbers


from itertools import permutations

def print_permutations(s):
    for p in permutations(s):
        print(''.join(p))

# Example usage
print_permutations('abc')  # Print permutations of 'abc'


def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# Example usage
print(reverse_sentence("We are ready"))  # "ready are We"


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Example usage
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False


def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

# Example usage
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True


import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Example usage
print(sphere_volume(5))  # Volume of a sphere with radius 5


def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst

# Example usage
print(unique_elements([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]


def is_palindrome(s):
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False


def histogram(lst):
    for num in lst:
        print('*' * num)

# Example usage
histogram([4, 9, 7])  # Prints the histogram


import random

def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    while guesses_taken < 6:
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    if guess == number:
        print(f"Good job, {name}! You guessed my number in
