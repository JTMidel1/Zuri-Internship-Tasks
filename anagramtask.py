# Zuri-Internship-Tasks
# Check if two words are anagrams

first_word = input(str("First Word: "))
second_word = input(str("Second Word:   "))


def find_anagram(first_word, second_word):
    
    if (sorted(first_word)) == sorted(second_word):
        print("True")
    else:
        print("False")

find_anagram(first_word, second_word)
