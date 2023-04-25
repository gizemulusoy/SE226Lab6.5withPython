print("-----------------Question 1 ----------------------------")
def common_elements(list1, list2):

    common = []

    for element in list1:

        if element in list2 and element not in common:

            common.append(element)


    return common
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = common_elements(list1, list2)

print(common)

print("------------------ Question 2 --------------------")

def palindrome_strings(strings):

    palindromes = []

    for string in strings:

        if string == string[::-1] and string != "":

            palindromes.append(string)


    return palindromes

strings = ["küçük", "level", "patates", "ada", "kart","fare"]

palindromes = palindrome_strings(strings)

print(palindromes)

print("-------------------Question3-----------------------")

def sieve_of_eratosthenes(numbers):
    primes = []
    is_prime = [True] * (max(numbers) + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(max(numbers) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max(numbers) + 1, i):
                is_prime[j] = False
    for number in numbers:
        if is_prime[number]:
            primes.append(number)
    return primes
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primes = sieve_of_eratosthenes(numbers)
print(primes)

print("-------------------Question 4 ------------------------")
from collections import Counter


def anagrams(word, word_list):

    counter_word = Counter(word.lower().replace(" ", ""))
    anagrams = []

    for string in word_list:
        counter_string = Counter(string.lower().replace(" ", ""))
        if counter_word == counter_string:
            anagrams.append(string)


    return anagrams

word = "logaritma"
word_list = ["algoritma", "matematik", "geometri", "problemler"]
anagram_list = anagrams(word, word_list)
print(anagram_list)
