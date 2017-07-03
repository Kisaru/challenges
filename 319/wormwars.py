#Worm wars
#S = number of susceptible
#I = number infectious (capable of spreading the pathogen)
#R = number recovered(immune)
#Total pop, initial infected, S to I, I to R, S to ReferenceError
#e.g. 10000 10 0.01 0.01 0.015

population = 10000
I = 10 #infected
S = 9990 #vulnerable
R = 0 #cured
SI = 0.01
IR = 0.01
SR = 0.015

i=0
while(S<10000):
	becoming_I = S*SI
	I = becoming_I+I
	S = S-becoming_I
	
	becoming_RfromI = I*IR
	R = becoming_RfromI+R
	I = I-becoming_RfromI
	
	becoming_RfromS = S*SR
	R = becoming_RfromS+R
	S = S-becoming_RfromS
	
print(I)
print(S)
print(R)
