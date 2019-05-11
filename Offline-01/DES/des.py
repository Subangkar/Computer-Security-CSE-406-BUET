import sys

import bitutils
import data

ENCODE = 1
DECODE = 0


class Des:
	def __init__(self):
		self.orig_key = None
		self.text = None
		self.keys = list()

	def encdec(self, key, text, action):
		self.text = text
		self.orig_key = key

		self.generatekeys()  # Generate all the keys for 16 iterations
		text_blocks = bitutils.nsplit(self.text, 8)  # Split the text in blocks of 8 bytes so 64 bits
		result = list()
		for block in text_blocks:
			block = bitutils.string_to_bit_array(block)
			block = self.permute(block, data.PI)  # initial permutation on data
			l, r = bitutils.nsplit(block, 32)  # l(LEFT), r(RIGHT)
			for i in range(16):  # Do the 16 iterations
				if action == ENCODE:
					k = self.keys[i]
				else:
					k = self.keys[15 - i]
				l_o = l
				l = r  # l(i) = r(i-1)
				r = bitutils.xor(l_o, self.f(r, k))  # r(i) = l(i-1) ^ r(i-1) ^ k(i)
			result += self.permute(r + l, data.PI_1)  # last permute to append to result
			self.text = bitutils.bit_array_to_string(result)

	def f(self, r, k):
		e = self.expand(r, data.E)  # Expand R to match Ki size (x48)
		return self.permute(bitutils.xor(k, e), data.P)  # (e ^ Ki)x48 into x32

	# Initial x56 key and x48 key_i for each iterations
	def generatekeys(self):
		self.keys = []
		key_x64 = bitutils.string_to_bit_array(self.orig_key)
		key_x56 = self.permute(key_x64, data.CP_1)  # x64 key to x56 key
		left, right = bitutils.nsplit(key_x56, 28)  # l,r (x28)
		for i in range(16):  # Apply the 16 rounds
			left, right = self.shift(left, right, data.SHIFT[i])
			ki_x56 = left + right
			ki_x48 = self.permute(ki_x56, data.CP_2)
			self.keys.append(ki_x48)  # Apply the permute in (x56) to get the Ki(x48)

	def permute(self, block, table):  # Permute the given block using the given table (so generic method)
		return [block[x - 1] for x in table]

	def expand(self, block, table):
		return self.permute(block, table)

	def shift(self, g, d, n):  # Shift a list of the given value
		return g[n:] + g[:n], d[n:] + d[:n]

	def encrypt(self, key, text):
		self.encdec(key, text, ENCODE)
		return self.text

	def decrypt(self, key, text):
		self.encdec(key, text, DECODE)
		return self.text


def addPadding(text):  # pad with \0
	pad_len = 8 - (len(text) % 8)
	if pad_len < 8:
		text += pad_len * '\0'
	return text, pad_len


def removePadding(text, pad_len):  # Remove the padding of the plain text (it assume there is padding)
	if pad_len > 0:
		return text[:-pad_len]
	else:
		return text


if __name__ == '__main__':
	sys.stdin = open("in.txt", "r")
	# key = "megabuck"
	# text = "Hello world"
	# key = input("Enter Key: ")
	# text = input("Enter Plain Text: ")

	key = input()
	text = input()
	print("Enter Key: " + key)
	print("Enter Plain Text: " + text)

	plain_text, pad_len = addPadding(text)
	d = Des()
	cipher_text = d.encrypt(key, plain_text)
	decrypted_text = removePadding(d.decrypt(key, cipher_text), pad_len)
	print("Key       : %r" % key)
	print("Ciphered  : %r" % cipher_text)
	print("Deciphered: %r" % decrypted_text)
