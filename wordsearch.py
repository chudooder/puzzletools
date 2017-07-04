import re
from itertools import permutations
from collections import defaultdict

f = open('words_alpha.txt')
dictionary = frozenset([w.strip() for w in f])

def find(word):
    if word in dictionary:
        print(word)

def find_pattern(pattern):
    comp = re.compile(pattern)
    for word in dictionary:
        if comp.fullmatch(word):
            print(word)

def find_fixed_length_pattern(pattern, length):
    comp = re.compile(pattern)
    for word in dictionary:
        if len(word) != length:
            continue
        if comp.fullmatch(word):
            print(word)

def letter_count(word):
    letters = defaultdict(int)
    total = 0
    for letter in word:
        letters[letter] += 1
        total += 1

    return letters

def perm_match(lc, letters, word):
    if len(word) != len(letters):
        return False
    wlc = letter_count(word)
    for ltr, cnt in lc.items():
        if ltr not in wlc:
            return False
        if wlc[ltr] < cnt:
            return False
    return True

def find_permute(letters):
    lc = letter_count([c for c in letters if c != '.'])
    results = []
    for word in dictionary:
        if perm_match(lc, letters, word):
            results.append(word)

    for w in sorted(results):
        print(w)
        