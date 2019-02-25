''' 
This program makes and displays a fibonacci sequence for a inputed 
amount it then prompts to add them. If accepted, it adds all the 
numbers in the sequence and displays it.
'''

## makes the list
global fib
global fib_for_sum
def fibonacci():
	'''Creates fibonacci sequence'''
	global fib 
	global fib_for_sum
	fib = [1]
	fib_for_sum = ''
	how_many = int(raw_input('How many times do you want to do this?\n'))
	print 'this is in the funtion'
	print how_many
	while how_many > 1:
		if len(fib) <= 1:
			fib += [1]
		else:
			fib += [fib[len(fib)-1]+fib[len(fib)-2]]
		how_many -= 1
	print fib
	fib_for_sum = fib
	sum_of_fibonacci()

## adds all of the numbers
def sum_of_fibonacci():
	Continue = raw_input('would you like to see the sum of all the numbers in the list you created above? (Y/N)\n')
	global fib_for_sum
	sum_of_fib = 0
	if Continue == 'y' or "Y" or "yes" or "Yes":
		for i in fib:
			sum_of_fib += i
	else:
		pass
	print '\nThe sum of your sequence is: ',sum_of_fib

#runs the program
fibonacci()

## to keep the program running
print '\n\n'
is_the_thing_running = raw_input('press enter to exit..' )
