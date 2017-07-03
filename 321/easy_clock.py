#Easy challenge 321. Converts a digital time into words
#Matthew Gall 29/06/2017

#00:00
#01:30
#12:05
#14:01
#20:29
#21:00

hour_set = ["one ", 
"two ", 
"three ", 
"four ", 
"five ", 
"six ", 
"seven ", 
"eight ",
"nine ",
"ten ",
"eleven ",
"twelve "]

minute_set = ["thirteen ", 
"fourteen ", 
"fifteen ", 
"sixteen ", 
"seventeen ", 
"eighteen ", 
"nineteen "]

minute_first = [
"twenty ",
"thirty ",
"fourty ",
"fifty "]

day = ["pm", "am"]

hour, minute = map(int, input().split(':'))

out = "It's "

if hour > 12:
	hour = hour - 12
out += hour_set[hour-1]


if minute < 13:
	out += "oh "
	out += hour_set[minute-1]
	
if minute > 12 & minute < 20:
	out = minute_set[minute-12]	
	
if minute > 20:
	first = int(minute[0])
	out += minute_first[first-2]
	
	second = int(minute[1])
	out += hour_set[second-1]	
	
if hour > 11:
	out += "pm"
else:
	out += "am"

print(out)
