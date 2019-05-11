def string_to_bit_array(text):  # Convert a string into a list of bits
	array = list()
	for char in text:
		binval = binvalue(char, 8)  # Get the char value on one byte
		array.extend([int(x) for x in list(binval)])  # Add the bits to the final list
	return array


def bit_array_to_string(array):  # Recreate the string from the bit array
	res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit(array, 8)]])
	return res


def binvalue(val, bitsize):  # Return the binary value as a string of the given size
	binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
	while len(binval) < bitsize:
		binval = "0" + binval  # Add as many 0 as needed to get the wanted size
	return binval


def nsplit(s, n):  # Split a list into sublists of size "n"
	return [s[k:k + n] for k in range(0, len(s), n)]


def xor(t1, t2):  # Apply a xor and return the resulting list
	return [x ^ y for x, y in zip(t1, t2)]
