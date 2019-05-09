import secondMostChar
import re

# ------------------ Data --------------------
orig_value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ------------------ INPUT --------------------
cipher_text = "THQVHAQCYCSPMAWARNTLNRTAVQUOEQWWNPQRTZQEYAWARTHQTENARTHQTENARKALLONWWMFINOQWTNTCAXQINKRVEQNTQTHQNXNLNRVHQKHQRTHQTENARLQNXQWTHQWTNTAYR "
clear_text = cipher_text
freq_chars = ['e', 't', 'a']
freq_words = ['atlantic', 'express', 'avalanche', 'station']

# ------------------ Map & Update --------------------
key_map = dict()
for char in orig_value:
	key_map[char] = '\0'


def updateMap(cipher, clear, key):
	for i in range(cipher.__len__()):
		if cipher[i] != clear[i] and clear[i].islower():
			if cipher[i].islower() or clear[i].isupper() or key[cipher[i]] != '\0':
				print("error", end="")
			else:
				key[cipher[i]] = clear[i]


# return key


def updatedClearTextWithMap(clear, key):
	for char in key:
		if key[char] != '\0':
			clear = clear.replace(char, key[char])
	return clear


# ------------------ Most Freq Chars Replacement --------------------
list_chars = (secondMostChar.char_count(cipher_text))

for i in range(freq_chars.__len__()):
	# print(freq_chars[i], end=' > ')
	# print(list_chars[-i - 1][0], end=' ')
	# print(list_chars[-i - 1][1], end='\n')
	key_map[list_chars[-i - 1][0]] = freq_chars[i]
	clear_text = clear_text.replace(list_chars[-i - 1][0], key_map[list_chars[-i - 1][0]])

# print(cipher_text)
# print(clear_text)
# ------------------ Word Replacement --------------------

# print(clear_text)
s = re.sub('at[A-Z]a[A-Z]t[A-Z][A-Z]', freq_words[0], clear_text)
# print(key_map)
updateMap(clear_text, s, key_map)
print(clear_text)
clear_text = updatedClearTextWithMap(clear_text, key_map)
# print(key_map)
# clear_text = re.sub('at[A-Z]a[A-Z]t[A-Z][A-Z]', freq_words[0], clear_text)
# print(cipher_text)
print(clear_text)
# import collections

# s = "helloworld"
# print(collections.Counter(s).most_common(1)[0])
