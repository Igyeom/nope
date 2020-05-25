"""

nope 1.1.1
A Programming Language developed by Ian Park
(not to mention the fact that this DESTROYS your brain)
(also inspired by the famous BRAINF***)

Documentation: https://docs.google.com/document/d/1VWU_x2yTWsPUMN_PM089eOVb-wE3FrPYGp0Kt6WTI0M/edit?usp=sharing

"""

def openF(f):
	data = open(f, "r").read()
	return data

def lex(f):
	tok = ""
	hiiii = list(f)
	ptr = 1
	var1 = 0
	var2 = 0
	var3 = 0
	var4 = 0
	char = 0
	for i in hiiii:
		tok += i
		char += 1
		if tok == "+":
			if ptr == 1:
				var1 += 1
			elif ptr == 2:
				var2 += 1
			elif ptr == 3:
				var3 += 1
			elif ptr == 4:
				var4 += 1
			tok = ""
		elif tok == "-":
			if ptr == 1:
				var1 -= 1
			elif ptr == 2:
				var2 -= 1
			elif ptr == 3:
				var3 -= 1
			elif ptr == 4:
				var4 -= 1
			tok = ""
		elif tok == ":":
			if ptr == 1:
				var1 += 10
			elif ptr == 2:
				var2 += 10
			elif ptr == 3:
				var3 += 10
			elif ptr == 4:
				var4 += 10
			tok = ""
		elif tok == ";":
			if ptr == 1:
				var1 -= 10
			elif ptr == 2:
				var2 -= 10
			elif ptr == 3:
				var3 -= 10
			elif ptr == 4:
				var4 -= 10
			tok = ""
		elif tok == "/":
			print("")
			tok = ""
		elif tok == "$":
			if ptr == 1:
				print(str(var1), end = "")
			elif ptr == 2:
				print(str(var2), end = "")
			elif ptr == 3:
				print(str(var3), end = "")
			elif ptr == 4:
				print(str(var4), end = "")
			tok = ""
		elif tok == "@":
			if ptr == 1:
				print(chr(var1), end = "")
			elif ptr == 2:
				print(chr(var2), end = "")
			elif ptr == 3:
				print(chr(var3), end = "")
			elif ptr == 4:
				print(chr(var4), end = "")
			tok = ""
		elif tok == "#":
			if ptr == 1:
				var1 = 0
			elif ptr == 2:
				var2 = 0
			elif ptr == 3:
				var3 = 0
			elif ptr == 4:
				var4 = 0
			tok = ""
		elif tok == "<":
			if ptr == 1:
				tok = ""
			else:
				ptr -= 1
				tok = ""
		elif tok == ">":
			if ptr == 4:
				tok = ""
			else:
				ptr += 1
				tok = ""
		elif tok == "=":
			print(str(ptr), end = "")
			tok = ""
		else:
			tok = ""
def run():
	print("Powered by Ian Park's nope 1.1.1")
	data = openF("main.nope")
	lex(data)

run()
