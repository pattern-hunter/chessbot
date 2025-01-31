def conv_ascii(s):
	result = ""
	for c in s:
		result += str(ord(c))
	return result