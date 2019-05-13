import sys

import bitutils
import data

ENCODE = 1
DECODE = 0


class DesEncryption:
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
		# permute x64 block into x64 using "PI"
		# run 16 iterations
		# permute result x64 to x64  using "PI_1"
		for block in text_blocks:
			block = bitutils.string_to_bit_array(block)
			block = self.permute(block, data.PI)  # initial permutation on data
			l, r = bitutils.nsplit(block, 32)  # l(LEFT), r(RIGHT)
			for i in range(16):  # 16 iterations
				if action == ENCODE:
					k = self.keys[i]
				else:
					k = self.keys[15 - i]
				l_o = l
				l = r  # l(i) = r(i-1)
				r = bitutils.xor(l_o, self.f(r, k))  # r(i) = l(i-1) ^ r(i-1) ^ k(i)
			result += self.permute(r + l, data.PI_1)  # last permute to append to result
			self.text = bitutils.bit_array_to_string(result)

	# extend R(i) x32 to  e x48 using "E"
	# f(R(i),K(i)) x48 into x32 using "PI_2"
	# permute that x32 into x32 using "P"
	def f(self, r, k):
		e = self.expand(r, data.E)  # Expand R to match Ki size (x48)
		f_x32 = self.permute(bitutils.xor(k, e), data.PI_2)  # (e ^ Ki)x48 into x32
		return self.permute(f_x32, data.P)

	# Initial x56 key and x48 key_i for each iterations
	# given x64 key to initial x56 key using "CP_1"
	# split initial x56 into two x28
	# shift two broken  x28 keys left  using "SHIFT"
	# merge into x56 and obtain x48 Ki using "CP_2"
	def generatekeys(self):
		self.keys = []
		key_x64 = bitutils.string_to_bit_array(self.orig_key)
		key_x56 = self.permute(key_x64, data.CP_1)  # x64 key to x56 key
		left, right = bitutils.nsplit(key_x56, 28)  # l,r (x28)
		for i in range(16):
			left, right = self.shift(left, right, data.SHIFT[i])
			ki_x56 = left + right
			ki_x48 = self.permute(ki_x56, data.CP_2)  # Apply the permute in (x56) to get the Ki(x48)
			self.keys.append(ki_x48)

	def permute(self, block, table):
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
	print("Enter Key        : %r" % key)
	print("Enter Plain Text : %r" % text)

	plain_text, pad_len = addPadding(text)
	d = DesEncryption()
	cipher_text = d.encrypt(key, plain_text)
	decrypted_text = removePadding(d.decrypt(key, cipher_text), pad_len)
	print("Key       : %r" % key)
	print("Ciphered  : %r" % cipher_text)
	print("Deciphered: %r" % decrypted_text)
