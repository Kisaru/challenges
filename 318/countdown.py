#Given a set of numbers X0-X5, calculate using mathematical operations to solve for Y. Y
#Can use addition, subtraction, multiplication, or division
#Order of operations is left to right
#E.g. 1 3 7 6 8 3 250
#3+8*7+6*3+1=250

input = [1,3,7,6,8,3,250]
Y = input[6]

numbers = input[0:6]#standard list from 1 to 6
out = input[0:6]#reorganised list

def operation(a,b,type):
	if type == 0:
		return a+b
	if type == 1:
		return a-b	 
	if type == 2:
		return a*b
	if type == 3:
		return a/b     

for a in range(6):#first number
	out[0] = numbers[a]#asign a number to first place
	del numbers[a]#remove that number from original list
	numbersfive = numbers[:]#remember the list for next iteration

	for b in range(5):#sceond number
		out[1] = numbersfive[b]
		del numbers[b]
		numbersfour = numbers[:]

		for c in range(4):#third number
			out[2] = numbersfour[c]
			del numbers[c]
			numbersthree = numbers[:]

			for d in range(3):#fourth number
				out[3] = numbersthree[d]
				del numbers[d]
				numberstwo = numbers[:]
				
				for e in range(2):#fifth number
					numbers = numberstwo[:]					
					out[4] = numberstwo[e]					
					del numbers[e]					
					
					#sixth number
					out[5] = numbers[0]
					
					for i in range(4):
						for j in range(4):
							for k in range(4):
								for l in range(4):
									for m in range(4):
										ab = operation(out[0],out[1],i)
										abc = operation(ab,out[2],j)
										abcd = operation(abc,out[3],k)
										abcde = operation(abcd,out[4],l)
										answer = operation(abcde,out[5],m)	
										if answer == Y:
											print(answer)
											print(out)
											print(i,j,k,l,m)
				numbers = numbersthree[:]
			numbers = numbersfour[:]
		numbers = numbersfive[:]
	numbers = input[0:6]#put number back6

