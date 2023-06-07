
# University of Michigan
# Coursera: Python 3 Programming Specialization
# Course 2: Python Functions, Files and Dictionaries
# Week 2: Chapter Dictionaries and Dictionary Accumulation
# Assessment: Dictionary Accumulation

# 1
# All the values of a dictionary are summed up and the result
# is assigned to a variable.

Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3, 'TO 313': 3,
          'BCOM 350': 1, 'MO 300': 3}

credits = 0
for k, v in Junior.items():
    credits += v

# 2
# A dictionary is created, which includes all characters of a string
# as a key and the value holds the frequency of that character.

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] += 1

# 3
# A dictionary is created, which includes all characters of a string
# as a key and the value holds the frequency of that character.

s1 = "hello"
counts = {}

for c in s1:
    if c not in counts:
        counts[c] = 0
    counts[c] += 1

# 4
# A dictionary is created, which includes all words of a string
# as a key and the value holds the frequency of that word.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
lst_str1 = str1.split()
freq_words = {}
for word in lst_str1:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1

print(freq_words)

# 5
# A dictionary is created, which includes all words of a string
# as a key and the value holds the frequency of that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
lst_sent = sent.split()
wrd_d = {}
for word in lst_sent:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] += 1

print(wrd_d)

# 6
# A dictionary is created, which includes all characters of a string
# as a key and the value holds the frequency of that character.
# The most frequent character is assigned to a variable.

sally = "sally sells sea shells by the sea shore"
characters = {}
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1

best_char_key = list(characters)[0]
for item in characters:
    if characters[item] > characters[best_char_key]:
        best_char_key = item

best_char = best_char_key

# 7
# A dictionary is created, which includes all characters of a string
# as a key and the value holds the frequency of that character.
# The least frequent character is assigned to a variable.

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1

worst_char = list(characters)[0]
for item in characters:
    if characters[item] < characters[worst_char]:
        worst_char = item

# 8
# A dictionary is created, which includes all characters of a string
# as a key and the value holds the frequency of that character.
# Characters should not be counted separately as upper-case and
# lower-case, instead saved as lower-case characters only.

string1 = "There is a tide in the affairs of men, Which taken at " \
          "the flood, leads on to fortune. Omitted, all the voyage " \
         "of their life is bound in shallows and in miseries. On " \
          "such a full sea are we now afloat. And we must take the " \
          "current when it serves, or lose our ventures."

letter_counts = {}
for c in string1:
    if c.lower() not in letter_counts:
        letter_counts[c.lower()] = 0
    letter_counts[c.lower()] += 1

# 9
# A dictionary is created, which includes all characters of a string
# as a key and the value holds the frequency of that character.
# Characters should not be counted separately as upper-case and
# lower-case, instead saved as lower-case characters only.

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p_lower = p.lower()
low_d = {}

for c in p_lower:
    if c not in low_d:
        low_d[c] = 0
    low_d[c] += 1
print(low_d)


