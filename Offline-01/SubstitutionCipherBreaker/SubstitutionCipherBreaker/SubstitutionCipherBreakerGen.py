import sys

import secondMostChar
import re

# ------------------ Data --------------------
cipher_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plain_chars = 'abcdefghijklmnopqrstuvwxyz'

cipher_text = ''
freq_chars_str = ''
freq_words_str = ''

freq_chars = []

freq_words = []
freq_words_custom = []

cipher_to_plain_map = dict()
plain_to_cipher_map = dict()
key_found_list = dict()


# ------------------ INPUT --------------------


def fileinput():
	global clear_text, cipher_text, freq_chars_str, freq_words_str, freq_words, freq_chars, freq_words_custom

	cipher_text = input()
	while freq_chars_str == '':
		freq_chars_str = input().strip()
	while freq_words_str == '':
		freq_words_str = input().strip()

	freq_words = freq_words_str.split(', ')
	freq_chars = freq_chars_str.split(', ')

	# cipher_text = "THQVHAQCYCSPMAWARNTLNRTAVQUOEQWWNPQRTZQEYAWARTHQTENARTHQTENARKALLONWWMFINOQWTNTCAXQINKRVEQNTQTHQNXNLNRVHQKHQRTHQTENARLQNXQWTHQWTNTAYR "
	# freq_chars = ['e', 't', 'a']
	# freq_words = ['atlantic', 'express', 'avalanche', 'station']

	clear_text = cipher_text
	with open('words.db', 'r') as f:
		for line in f:
			for word in line.split():
				if word == '#':
					return
				freq_words_custom.append(word)


# ------------------ Map & Update --------------------

def initmap():
	global cipher_to_plain_map, key_found_list, cipher_chars
	for i in range(26):
		key_found_list[str(chr(i + ord('a')))] = False
	for char in cipher_chars:
		cipher_to_plain_map[char] = '\0'
	for char in plain_chars:
		plain_to_cipher_map[char] = '\0'


def addmapping(decoded_char, encoded_char):
	global cipher_to_plain_map, plain_to_cipher_map, key_found_list
	cipher_to_plain_map[encoded_char] = decoded_char
	plain_to_cipher_map[decoded_char] = encoded_char
	key_found_list[decoded_char] = True


def updateMap(cipher, clear, key, key_found):
	for i in range(cipher.__len__()):
		if cipher[i] != clear[i] and clear[i].islower():
			if cipher[i].isupper() and clear[i].islower() and key[cipher[i]] == '\0':
				addmapping(clear[i], cipher[i])


# else:
# 	print("redundant > ", end=" ")
# 	print("cipher=" + cipher[i], end=" ")
# 	print("clear=" + clear[i], end=" ")
# 	print("key=" + key[cipher[i]], end="\n")


def updatedClearTextWithMap(clear, key):
	for char in key:
		if key[char] != '\0':
			clear = clear.replace(char, key[char])
	return clear


def printmapping(charset, key):
	for c in charset:
		print(c, end=" ")
	print()

	count = 0
	for c in charset:
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


def encode(text, key):
	encoded = ""
	for c in text:
		if c in key:
			encoded += key[c]
		else:
			encoded += c
	return encoded


# ------------------ Most Freq Chars Replacement --------------------
def replacefreqletters():
	global cipher_to_plain_map, key_found_list, clear_text, cipher_text, freq_words, freq_chars

	# print(clear_text)  # Cipher

	freq_count_list = (secondMostChar.char_count(cipher_text))

	for i in range(freq_chars.__len__()):
		addmapping(freq_chars[i], freq_count_list[-i - 1][0])
		clear_text = clear_text.replace(freq_count_list[-i - 1][0], cipher_to_plain_map[freq_count_list[-i - 1][0]])


# print(clear_text)  # frequent Replaced

# ------------------ Word Replacement Provided --------------------

def replaceprovidedwords():
	global cipher_to_plain_map, key_found_list, clear_text, cipher_text, freq_words, freq_chars

	# print(freq_pattern[freq_words[0]])
	for i in range(freq_words.__len__()):
		print(freq_words[i], end=">>")
		print(string_to_regex(freq_words[i], key_found_list))
		s = re.sub(string_to_regex(freq_words[i], key_found_list), freq_words[i], clear_text)
		# print(s)  # frequent Replaced
		updateMap(clear_text, s, cipher_to_plain_map, key_found_list)
		clear_text = updatedClearTextWithMap(clear_text, cipher_to_plain_map)
	# print(clear_text)  # word 1 replaced

	print("\n --------- From Provided Words Only ---------- ")
	print("Key: ")
	printmapping(cipher_chars, cipher_to_plain_map)
	print("Cipher: " + cipher_text)
	print("Clear : " + clear_text)
	print("Cipher: " + encode(clear_text, plain_to_cipher_map))


# ------------------ Word Replacement Custom --------------------
def replacecustomwords():
	global cipher_to_plain_map, key_found_list, clear_text, cipher_text, freq_words, freq_chars

	if len(freq_words_custom) == 0:
		return

	# print(freq_pattern[freq_words[0]])
	for i in range(freq_words_custom.__len__()):
		print(freq_words_custom[i], end=">>")
		print(string_to_regex(freq_words_custom[i], key_found_list))
		s = re.sub(string_to_regex(freq_words_custom[i], key_found_list), freq_words_custom[i], clear_text)
		# print(s)  # frequent Replaced
		updateMap(clear_text, s, cipher_to_plain_map, key_found_list)
		clear_text = updatedClearTextWithMap(clear_text, cipher_to_plain_map)
	# print(clear_text)  # word 1 replaced

	print("\n --------- From Visible Intuition ---------- ")
	print("Key: ")
	printmapping(cipher_chars, cipher_to_plain_map)
	print("Cipher: " + cipher_text)
	print("Clear : " + clear_text)
	print("Cipher: " + encode(clear_text, plain_to_cipher_map))


if __name__ == '__main__':
	sys.stdin = open("in/substitution-15.txt", "r")
	fileinput()
	initmap()
	replacefreqletters()
	replaceprovidedwords()
	replacecustomwords()
	print("Cipher to Plain:")
	printmapping(cipher_chars, cipher_to_plain_map)
	print("Plain to Cipher:")
	printmapping(plain_chars, plain_to_cipher_map)
