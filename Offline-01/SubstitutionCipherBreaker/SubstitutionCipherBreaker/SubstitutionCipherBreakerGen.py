import secondMostChar
import re

# ------------------ Data --------------------
orig_value = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ------------------ INPUT --------------------
cipher_text = "THQVHAQCYCSPMAWARNTLNRTAVQUOEQWWNPQRTZQEYAWARTHQTENARTHQTENARKALLONWWMFINOQWTNTCAXQINKRVEQNTQTHQNXNLNRVHQKHQRTHQTENARLQNXQWTHQWTNTAYR "
clear_text = cipher_text

freq_chars = ['e', 't', 'a']

freq_words = ['atlantic', 'express', 'avalanche', 'station']

freq_words_custom = [
	'and'
	# ,'ing'
	,'will'
	,'of'
	# ,'be'
	# ,'by'
	,'passby'
	, 'dawn'
]

# ------------------ Map & Update --------------------
key_map = dict()
key_found_list = dict()
for i in range(26):
	key_found_list[str(chr(i + ord('a')))] = False
for char in orig_value:
	key_map[char] = '\0'


def updateMap(cipher, clear, key, key_found):
	for i in range(cipher.__len__()):
		if cipher[i] != clear[i] and clear[i].islower():
			if cipher[i].islower() or clear[i].isupper() or key[cipher[i]] != '\0':
				print("redundant > ", end=" ")
				print("cipher=" + cipher[i], end=" ")
				print("clear=" + clear[i], end=" ")
				print("key=" + key[cipher[i]], end="\n")
			else:
				key[cipher[i]] = clear[i]
				key_found[clear[i]] = True


def updatedClearTextWithMap(clear, key):
	for char in key:
		if key[char] != '\0':
			clear = clear.replace(char, key[char])
	return clear


def printkey(key):
	for c in orig_value:
		print(c, end=" ")
	print()

	count = 0
	for c in orig_value:
		if key[c] != '\0':
			print(key[c], end=" ")
		else:
			count += 1
			print(' ', end=" ")
	print("\n" + str(count) + ' Undetected')


def string_to_regex(word, key_found_list):
	regex = ""
	for c in word:
		if c in key_found_list and key_found_list[c]:
			regex += c
		else:
			regex += '[A-Z]'
	return regex


# ------------------ Most Freq Chars Replacement --------------------
# print(clear_text)  # Cipher

freq_count_list = (secondMostChar.char_count(cipher_text))

for i in range(freq_chars.__len__()):
	key_map[freq_count_list[-i - 1][0]] = freq_chars[i]
	key_found_list[freq_chars[i]] = True
	clear_text = clear_text.replace(freq_count_list[-i - 1][0], key_map[freq_count_list[-i - 1][0]])

# print(clear_text)  # frequent Replaced
# ------------------ Word Replacement Provided --------------------

# print(freq_pattern[freq_words[0]])
for i in range(freq_words.__len__()):
	print(freq_words[i], end=" ")
	print(string_to_regex(freq_words[i], key_found_list))
	s = re.sub(string_to_regex(freq_words[i], key_found_list), freq_words[i], clear_text)
	# print(s)  # frequent Replaced
	updateMap(clear_text, s, key_map, key_found_list)
	clear_text = updatedClearTextWithMap(clear_text, key_map)
# print(clear_text)  # word 1 replaced

print("\n --------- From Provided Words Only ---------- ")
print("Key: ")
printkey(key_map)
print("Cipher: " + cipher_text)
print("Clear : " + clear_text)

# ------------------ Word Replacement Custom --------------------

# print(freq_pattern[freq_words[0]])
for i in range(freq_words_custom.__len__()):
	print(freq_words_custom[i], end=" ")
	print(string_to_regex(freq_words_custom[i], key_found_list))
	s = re.sub(string_to_regex(freq_words_custom[i], key_found_list), freq_words_custom[i], clear_text)
	# print(s)  # frequent Replaced
	updateMap(clear_text, s, key_map, key_found_list)
	clear_text = updatedClearTextWithMap(clear_text, key_map)
# print(clear_text)  # word 1 replaced

print("\n --------- From Visible Intuition ---------- ")
print("Key: ")
printkey(key_map)
print("Cipher: " + cipher_text)
print("Clear : " + clear_text)

# # printkey(key_map)
# # s = "helloworld"
# # print(collections.Counter(s).most_common(1)[0])
