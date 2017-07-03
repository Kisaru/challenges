#Implements the Collatz Conjecture tag system described here: https://en.wikipedia.org/wiki/Tag_system#Example:_Computation_of_Collatz_sequences

m = 2 #deletion number (tag)
#alphabet = [a,b,c] #finite set of symbols
n = "aaaaaaa" #input

#Production rules for tag system
def prod_rules(letter):
	if letter == "a":
		output = "bc"
	elif letter == "b":
		output = "a"
	elif letter == "c":
		output = "aaa"
	return output

#Halt when system tends to 1 letter
while(len(n) != 1):
	letter = n[0]#Take first letter
	new = n[2:]#Delete first 2 letters
	n = new + prod_rules(letter)#Add on new letters based on production rules
	print(n)#Print current string