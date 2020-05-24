"""

nope 1.0
A Programming Language developed by Ian Park
(not to mention the fact that this DESTROYS your brain)
(also inspired by the famous BRAINF#@%)

Documentation: https://docs.google.com/document/d/1VWU_x2yTWsPUMN_PM089eOVb-wE3FrPYGp0Kt6WTI0M/edit?usp=sharing

"""

def openF(f):
  data = open(f, "r").read()
  return data

def lex(f):
  tok = ""
  hiiii = list(f)
  vi = False
  var = 0;
  for i in hiiii:
    tok += i
    if tok == "+":
      var += 1
      tok = ""
    elif tok == ":":
      var += 10
      tok = ""
    elif tok == "-":
      var -= 1
      tok = ""
    elif tok == ";":
      var -= 10
      tok = ""
    elif tok == "/":
      print("")
      tok = ""
    elif tok == "$":
      print(str(var), end = "")
      tok = ""
    elif tok == "@":
      print(chr(var), end = "")
      tok = ""
    elif tok == "#":
      var = 0
      tok = ""
    else:
      print("Error: Invalid character!")
      break
def run():
  print("Powered by Ian Park's nope 1.0")
  data = openF("main.nope")
  lex(data)

run()
