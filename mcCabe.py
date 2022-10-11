import os
import sys


def mcCabe(file):
	#print(file)
	if(file.endswith('.java')):
			f = open(file)
			finalCount = complexityCounter(f.readlines())
			f.close()

			return finalCount

def complexityCounter(f):
	count = 1
	for line in f:
		if(" if " in line or "while " in line or " for " in line or "switch " in line):
			if("*" not in line and "/" not in line and "//" not in line and '"' not in line ):
				count+=1
	return count


def start(string):
	if (not isinstance(string, str)):
		return f"{string}"
	else:
		return string


def result(string):
	#print(string)
	out = mcCabe(start(string))
	#print(out)
	return out 

if __name__ == "__main__":
   result(sys.argv[1])
