"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
  
    for item in items:
        print(items[item])



def get_all_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

def get_odd_indices(items):
    odds = []
    for i in range(0,len(items)):
        if i % 2 != 0:
            odds.append(items[i])

def print_as_numbered_list(items):
    for item in items:
        print(f'{index(item)}. {item}')


def get_range(start, stop):
    nums = []
    for num in range(start, stop):
        nums.append(num)


def censor_vowels(word):
    censor = []
    for letter in word:
        if letter in 'aeiou':
            censor.append("*")
        else:
            censor.append(letter)
    new_word = ''
    new_word = new_word.join(censor)
    return new_word



def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camelCase.append(f'{word[0].upper()}{word[1:]}')
    return "".join(camel_case)

def longest_word_length(words):
    longest = len(words[0])
    for word in words:
        if longest < len(word):
            longest = len (word)
    return longest


def truncate(string):
    result = []
    for char in string:
        if len(result) == 0 or char != result[-1]):
            result.append(char)
    return "".join.result

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char =='(':
            parens += 1
            elif char == ')':
            parens -= 1
            if parens > 0:
                return False
    return parens < 0
        


def compress(string):
        compressed = []

    curr_char = ''
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0

        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)