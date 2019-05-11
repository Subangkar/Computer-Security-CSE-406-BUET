import bitstring
import data

ENCODE = 1
DECODE = 0


class Des:
	def __init__(self):
		self.password = None
		self.text = None
		self.pad_len = 0
		self.keys = list()

	def encdec(self, key, text, action):
		self.text = text
		self.password = key

		self.generatekeys()  # Generate all the keys for 16 iterations
		text_blocks = bitstring.nsplit(self.text, 8)  # Split the text in blocks of 8 bytes so 64 bits
		result = list()
		for block in text_blocks:  # Loop over all the blocks of data
			block = bitstring.string_to_bit_array(block)  # Convert the block in bit array
			block = self.permut(block, data.PI)  # Apply the initial permutation
			g, d = bitstring.nsplit(block, 32)  # g(LEFT), d(RIGHT)
			tmp = None
			for i in range(16):  # Do the 16 rounds
				d_e = self.expand(d, data.E)  # Expand d to match Ki size (48bits)
				if action == ENCODE:
					tmp = self.xor(self.keys[i], d_e)  # If encrypt use Ki
				else:
					tmp = self.xor(self.keys[15 - i], d_e)  # If decrypt start by the last key
				tmp = self.permut(tmp, data.P)
				tmp = self.xor(g, tmp)
				g = d
				d = tmp
			result += self.permut(d + g, data.PI_1)  # Do the last permut and append the result to result
		self.text = bitstring.bit_array_to_string(result)

	# Initial x56 key and x48 key_i for each iterations
	def generatekeys(self):
		self.keys = []
		key = bitstring.string_to_bit_array(self.password)
		key = self.permut(key, data.CP_1)  # Apply the initial permut on the key
		g, d = bitstring.nsplit(key, 28)  # Split it in to (g->LEFT),(d->RIGHT)
		for i in range(16):  # Apply the 16 rounds
			g, d = self.shift(g, d, data.SHIFT[i])  # Apply the shift associated with the round (not always 1)
			tmp = g + d  # Merge them
			self.keys.append(self.permut(tmp, data.CP_2))  # Apply the permut to get the Ki

	def permut(self, block, table):  # Permut the given block using the given table (so generic method)
		return [block[x - 1] for x in table]

	def expand(self, block, table):  # Do the exact same thing than permut but for more clarity has been renamed
		return [block[x - 1] for x in table]

	def shift(self, g, d, n):  # Shift a list of the given value
		return g[n:] + g[:n], d[n:] + d[:n]

	def xor(self, t1, t2):  # Apply a xor and return the resulting list
		return [x ^ y for x, y in zip(t1, t2)]

	def encrypt(self, key, text):
		self.encdec(key, text, ENCODE)
		return self.text

	def decrypt(self, key, text):
		self.encdec(key, text, DECODE)
		return self.text


def addPadding(text):  # pad with \0.
	pad_len = 0
	if len(text) % 8 != 0:
		pad_len = 8 - (len(text) % 8)
	text += pad_len * '0'
	return text, pad_len


def removePadding(text, pad_len):  # Remove the padding of the plain text (it assume there is padding)
	if pad_len > 0:
		return text[:-pad_len]
	else:
		return text


if __name__ == '__main__':
	# key = "megabuck"
	# text = "Hello world"
	key = input("Enter Key: ")
	text = input("Enter Plain Text: ")
	plain_text, pad_len = addPadding(text)
	d = Des()
	cipher_text = d.encrypt(key, plain_text)
	decrypted_text = removePadding(d.decrypt(key, cipher_text), pad_len)
	print("Key       : %r" % key)
	print("Ciphered  : %r" % cipher_text)
	print("Deciphered: %r" % decrypted_text)
