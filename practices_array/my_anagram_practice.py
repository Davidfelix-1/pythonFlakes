def is_anagram(s1, s2):
    s1 = s1.replace(" ", " ").lower()
    s2 = s2.replace(" ", " ").lower()
    return sorted(s1) == sorted(s2)


my_first_word = "Listen"
my_second_word = "Silent"

if is_anagram(my_first_word, my_second_word):
    print("the strings are anagrams")
else:
    print("not the strings are not anagrams")
