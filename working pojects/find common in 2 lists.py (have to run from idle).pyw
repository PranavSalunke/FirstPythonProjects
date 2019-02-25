#create 2 lists and find common values

import random
def com(n,m):
	'''n = number of objects in list;	m = random int 0 --> m'''
	x = 0
	l = []
	l2 = []
	l3 = []
	while x != n:
		l += [random.randint(0,m)]
		l2 += [random.randint(0,m)]
		x += 1
	for i in l:
		for r in l2:
                        
			if r == i:
				l3 += [i]
			else:
				l3 = l3
	print 'FIRST LIST:' ,l
	print 'SECOND LIST:' ,l2
	print ('common: ')
	print list(set(l3))

def settings_for_com():
        print 'n is number of objects in list\n'
        n = raw_input('what do you want the value of \'n\' to be?\n')
        print 'm is the last number in the set that a random number will be picked from. 0 --> m'
        m = raw_input('what do you want the value of \'m\' to be?\n')
        print '\n'
        com(int(n),int(m))
        
settings_for_com()

# to keep the program on:
to_keep_prog_on = raw_input()
