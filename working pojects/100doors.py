###100 doors problem###

doors=['not a door']
which_doors = []
person = 0
number_of_doors = 0
opened = 0

def set_100_closed_doors():
	global doors
	global number_of_doors
	number_of_doors = raw_input('how many doors?	')
	while len(doors) < (int(number_of_doors)+1):
		doors.append(0)
	return doors

def people():
	global person 
	person += 1
	return person

def door_numbers():
	global person
	global which_doors
	global number_of_doors
	which_doors = range(0,int(number_of_doors)+1,person)
	return which_doors


def go_through_doors():
	global which_doors
	global doors
	for i in which_doors:
		door = doors[i]
		if door == 0:
			doors[i] = 1
		elif door == 1:
			doors[i] = 0
		else:
			pass
	return doors 
	return which_doors

def find_open():
	global doors
	global opened
	for i in doors:
		if i == 1:
			opened += 1
	print "These many doors are left open after the last person goes through: " + str(opened)

def solve_problem():
	global person
	global doors
	set_100_closed_doors()
	while person <= len(doors):
		people()
		door_numbers()
		go_through_doors()
	print 'done!'
	print doors
	print (" ")
	find_open()

solve_problem()



## to keep the program running
print '\n\n'
is_the_thing_running = raw_input('press enter to exit..' )
