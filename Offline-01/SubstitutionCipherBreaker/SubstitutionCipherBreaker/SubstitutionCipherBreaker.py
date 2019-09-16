import secondMostChar
import re

# ------------------ Data --------------------
cipher_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# ------------------ INPUT --------------------
cipher_text = "THQVHAQCYCSPMAWARNTLNRTAVQUOEQWWNPQRTZQEYAWARTHQTENARTHQTENARKALLONWWMFINOQWTNTCAXQINKRVEQNTQTHQNXNLNRVHQKHQRTHQTENARLQNXQWTHQWTNTAYR "
clear_text = cipher_text

freq_chars = ['e', 't', 'a']

freq_words = ['atlantic', 'express', 'avalanche', 'station']
freq_pattern = {'atlantic': 'at[A-Z]a[A-Z]t[A-Z]{2}'
	, 'express': re.compile(r'e[A-Z]{3}e([A-Z])\1')
	, 'avalanche': 'a[A-Z]alanc[A-Z]e'
	, 'station': 'stati[A-Z]n'
                }

freq_words_custom = [
	'and',
	# 'ing',
	'will',
	'of',
	# 'be',
	# 'by',
	'passby'
]

freq_pattern_custom = {
	'and': 'an[A-Z]'
	# , 'ing': 'in[A-Z]'
	, 'will': '[A-Z]ill'
	, 'of': 'o[A-Z]'
	# , 'be': '[A-Z]e'
	# , 'by': 'b[A-Z]'
	, 'passby': 'pass[A-Z]{2}'
}

# ------------------ Map & Update --------------------
cipher_to_plain_map = dict()
for char in cipher_chars:
	cipher_to_plain_map[char] = '\0'


def updateMap(cipher, clear, key):
	for i in range(cipher.__len__()):
		if cipher[i] != clear[i] and clear[i].islower():
			if cipher[i].islower() or clear[i].isupper() or key[cipher[i]] != '\0':
				print("redundant > ", end=" ")
				print("cipher=" + cipher[i], end=" ")
				print("clear=" + clear[i], end=" ")
				print("key=" + key[cipher[i]], end="\n")
			else:
				key[cipher[i]] = clear[i]


def updatedClearTextWithMap(clear, key):
	for char in key:
		if key[char] != '\0':
			clear = clear.replace(char, key[char])
	return clear


def printkey(key):
	for c in cipher_chars:
		print(c, end=" ")
	print()

	count = 0
	for c in cipher_chars:
		if key[c] != '\0':
			print(key[c], end=" ")
		else:
			count += 1
			print(' ', end=" ")
	print("\n" + str(count) + ' Undetected')


# ------------------ Most Freq Chars Replacement --------------------
print(clear_text)  # Cipher

freq_count_list = (secondMostChar.char_count(cipher_text))

for i in range(freq_chars.__len__()):
	# print(freq_chars[i], end=' > ')
	# print(freq_count_list[-i - 1][0], end=' ')
	# print(freq_count_list[-i - 1][1], end='\n')
	cipher_to_plain_map[freq_count_list[-i - 1][0]] = freq_chars[i]
	clear_text = clear_text.replace(freq_count_list[-i - 1][0], cipher_to_plain_map[freq_count_list[-i - 1][0]])

print(clear_text)  # frequent Replaced

# ------------------ Word Replacement Provided --------------------

# print(freq_pattern[freq_words[0]])
for i in range(freq_words.__len__()):
	s = re.sub(freq_pattern[freq_words[i]], freq_words[i], clear_text)
	print(s)  # frequent Replaced
	updateMap(clear_text, s, cipher_to_plain_map)
	clear_text = updatedClearTextWithMap(clear_text, cipher_to_plain_map)
	print(clear_text)  # word 1 replaced

print("\n --------- From Provided Words Only ---------- ")
print("Key: ")
printkey(cipher_to_plain_map)
print("Cipher: " + cipher_text)
print("Clear : " + clear_text)

# ------------------ Word Replacement Custom --------------------

# print(freq_pattern[freq_words[0]])
for i in range(freq_words_custom.__len__()):
	s = re.sub(freq_pattern_custom[freq_words_custom[i]], freq_words_custom[i], clear_text)
	print(s)  # frequent Replaced
	updateMap(clear_text, s, cipher_to_plain_map)
	clear_text = updatedClearTextWithMap(clear_text, cipher_to_plain_map)
	print(clear_text)  # word 1 replaced

print("\n --------- From Visible Intuition ---------- ")
print("Key: ")
printkey(cipher_to_plain_map)
print("Cipher: " + cipher_text)
print("Clear : " + clear_text)

# printkey(key_map)
# s = "helloworld"
# print(collections.Counter(s).most_common(1)[0])
