import bitstring
import data


class Des:
	def __init__(self):
		self.password = None
		self.text = None
		self.keys = list()
		self.pad_len = 0

	def encrypt(self, key, text):
		self.text = text
		self.password = key

		self.addPadding()

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
				tmp = self.xor(self.keys[i], d_e)  # If encrypt use Ki
				# tmp = self.substitute(tmp)  # Method that will apply the SBOXes
				tmp = self.permut(tmp, data.P)
				tmp = self.xor(g, tmp)
				g = d
				d = tmp
			result += self.permut(d + g, data.PI_1)  # Do the last permut and append the result to result

		self.removePadding()

	def addPadding(self):  # pad with \0.
		if len(self.text) % 8 != 0:
			self.pad_len = 8 - (len(self.text) % 8)
		self.text += self.pad_len * '\0'

	def removePadding(self):  # Remove the padding of the plain text (it assume there is padding)
		if self.pad_len > 0:
			self.text = self.text[:-self.pad_len]

	def generatekeys(self):  # Algorithm that generates all the keys
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


if __name__ == '__main__':
	key = "megabuck"  # "secret_k"
	text = "Hello world12345"
	d = Des()
	r = d.encrypt(key, text)
	# r2 = d.decrypt(key, r, True)
	print("Key       : %r" % key)
	print("Ciphered  : %r" % r)
# print("Deciphered: %r" % r2)
