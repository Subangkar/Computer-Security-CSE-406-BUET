import secondMostChar

# ------------------ Data --------------------
orig_value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ------------------ INPUT --------------------
cipher_text = "THQVHAQCYCSPMAWARNTLNRTAVQUOEQWWNPQRTZQEYAWARTHQTENARTHQTENARKALLONWWMFINOQWTNTCAXQINKRVEQNTQTHQNXNLNRVHQKHQRTHQTENARLQNXQWTHQWTNTAYR "
clear_text = cipher_text
freq_chars = ['e', 't', 'a']
freq_words = ['atlantic', 'express', 'avalanche', 'station']

# ------------------ Map --------------------
key_map = dict()
for char in orig_value:
	key_map[char] = '\0'

# ------------------ Most Freq Chars Replacement --------------------
list_chars = (secondMostChar.char_count(cipher_text))

for i in range(freq_chars.__len__()):
	print(freq_chars[i], end=' > ')
	print(list_chars[-i - 1][0], end=' ')
	print(list_chars[-i - 1][1], end='\n')
	key_map[list_chars[-i - 1][0]] = freq_chars[i]
	clear_text = clear_text.replace(list_chars[-i - 1][0], key_map[list_chars[-i - 1][0]])

print(cipher_text)
print(clear_text)
# ------------------ Word Replacement --------------------

# import collections

# s = "helloworld"
# print(collections.Counter(s).most_common(1)[0])
