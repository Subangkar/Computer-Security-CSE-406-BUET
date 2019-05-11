def string_to_bit_array(text):
	array = list()
	for char in text:
		binval = binvalue(char, 8)
		array.extend([int(x) for x in list(binval)])
	return array


def bit_array_to_string(array):
	res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit(array, 8)]])
	return res


def nsplit(s, n):  # sub-lists are of size "n"
	return [s[k:k + n] for k in range(0, len(s), n)]


def binvalue(val, bitsize):  # Return the binary value as a string of the given size
	binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
	while len(binval) < bitsize:
		binval = "0" + binval
	return binval


def xor(t1, t2):
	return [x ^ y for x, y in zip(t1, t2)]
