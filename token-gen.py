# made by jlcl#0092

import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

for i in range(100): # Number Of Tokens To Gen
	first = ''.join((random.choice(chars) for i in range(24)))
	second = ''.join((random.choice(chars) for i in range(6)))
	third = ''.join((random.choice(chars) for i in range(27)))

	result = first + "." + second + "." + third

	output = open("tokens.txt", "a") # saving to output.txt
	output.write(result + "\n")