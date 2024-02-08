def grams_to_ounces(grams):
    return grams / 28.3495231



def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)




def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]




from itertools import permutations

def print_permutations(s):
    for p in permutations(s):
        print(''.join(p))



def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])




def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False



def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1




import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3




def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst




def is_palindrome(s):
    return s == s[::-1]




def histogram(lst):
    for num in lst:
        print('*' * num)




import random

def guess_the_number():
    number = random.randint(1, 20)
    name = input("Hello! What is your name?\n")

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
        print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {number}.")



