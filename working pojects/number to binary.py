

def find_binary():
	number = int(raw_input("What is your number?\n"))
	global list_of_remainders
	list_of_remainders = []
	while number > 0:
		mod = [number%2]
		list_of_remainders += mod
		number = number/2
	return list_of_remainders

def backward():
	correct_way = []
	x = 1
	i = len(list_of_remainders)-1
	while x< len(list_of_remainders)+1:
		correct_way += [list_of_remainders[i]]
		x+=1
		i-=1
	print "the correct way is:"
	print correct_way



#run the program
find_binary()
backward()

## to keep the program running
print '\n\n'
is_the_thing_running = raw_input('press enter to exit..' )
