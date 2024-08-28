#!/usr/bin/env python3

def return_evens(num_list):
     return [num for num in num_list if num % 2 == 0]

# Test case
print(return_evens([0, 2, 4, 6, 8]))  
pass

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

print(make_exclamation(["Hello", "I like computers","I require coffee","Live long and prosper",]))  

pass