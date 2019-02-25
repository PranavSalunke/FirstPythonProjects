### THIS IS THE SECOND VERSON###
## grade book ##


## global list of students 
list_student = []
## global list of the objects of each student. This holds the values.
list_studentObj = []
##
index_for_student = 'nothing'
##bluprint for Student
class Student():
	def __init__(self, name, grade, test, hw, participation, project):
		self.name = name
		self.grade = grade
		self.test = test
		self.hw = hw
		self.part = participation
		self.proj = project
	def name(self):
		return self.name
	def grade(self):
		return self.grade
	def test(self):
		return self.test
	def hw(self):
		return self.hw
	def participation(self):
		return self.part
	def project(self):
		return self.proj

## global value for nameObj
nameObj = Student(' ',0,0,0,0,0)

## set the info for student
def set_student(): # hold
	global list_student
	global nameObj
	global list_studentObj
	print 'lets set up the studnet'
	name = raw_input('what is the name of the sudent?\n')
	g = raw_input('what is the student\'s letter grade?\n')
	t = raw_input('what is the sudent\'s test grade in percentage?\n')
	h = raw_input('what is the student\'s homework grade in percentage?\n')
	pa = raw_input('what is the student\'s participation grade in percentage?\n')
	pr = raw_input('what is the student\'s project grade in percentage\n')
	print ('\n\n')
	nameObj = Student(name, g, t, h, pa, pr)


	
##ask to look at directory 
	list_student += [name]
	list_studentObj += [nameObj]   ## NOTE: this is the object. when find_student() is called it will find the index value for the name by a name input. that index (i) will be passed down to find_info(). It will use that index value in list_studentObj  to acces the methods of the class. 
	directory = str(raw_input( 'want to see the list of students? Y/N\n')) 
	if directory == 'Y' or 'y':
		print (list_student)
		access_dir = raw_input('do you want to access the directory? Y/N\n')
		if access_dir == 'Y' or 'y':
			access_d()

## funtion to access the directory 
def access_d():
	print list_student,' \n'
	this_student = raw_input ('which student do you want to check?\n')
	find_student(this_student)

##funtion to match  student value in list with the student in question.
def find_student(this_stu):
	global index_for_student
	index_for_student = 0
	which_student = this_stu
	for i in range( len(list_student)):
		if which_student == list_student[i]:
			index_for_student = i
		else:
			pass
	find_info()
##funtion for finding specific atrubutes (methods) for the student in question.
def find_info():
        global index_for_student
        want = raw_input('what do you want to see? 1)all, 2)name, 3)grade, 4)test, 5)hw, 6)participation, 7)project? chose one 1-7.\n' )
        current_student = list_studentObj[index_for_student]
        if want == 'all' or 1:
        	print '\nname: ',current_student.name, '\ngrade: ', current_student.grade, '\ntest: ', current_student.test, '\nhomework: ', current_student.hw, '\nparticipation: ', current_student.participation, '\nproject: ', current_student.project
        pass # for now (code to come later)

## actuall program to run. 
keep_going = 'Y' or 'y'

while keep_going == 'Y' or 'y':
        set_student()
        keep_going = str(raw_input('want to keep going? Y/N\n'))
        if keep_going != 'Y' or 'y':
                break



## to keep the program running
print '\n\n'
is_the_thing_running = raw_input('press enter to exit..' )




'''
## global list of students 
list_student = []
## global list of the objects of each student. This holds the values.
list_studentObj = []
##
index_for_student = 'nothing'
##bluprint for Student
class Student():
	def __init__(self, name, grade, test, hw, participation, project):
		self.name =
		self.grade = grade
		self.test = test
		self.hw = hw
		self.part = participation
		self.proj = project
	def name(self):
		return self.name
	def grade(self):
		return self.grade
	def test(self):
		return self.test
	def hw(self):
		return self.hw
	def participation(self):
		return self.part
	def project(self):
		return self.proj

## global value for nameObj
nameObj = Student(' ',0,0,0,0,0)

## set the info for student
def set_student(): # hold
	global list_student
	global nameObj
	global list_studentObj
	print 'lets set up the studnet'
	name = raw_input('what is the name of the sudent?\n')
	g = raw_input('what is the student\'s letter grade?\n')
	t = raw_input('what is the sudent\'s test grade in percentage?\n')
	h = raw_input('what is the student\'s homework grade in percentage?\n')
	pa = raw_input('what is the student\'s participation grade in percentage?\n')
	pr = raw_input('what is the student\'s project grade in percentage\n')
	print ('\n\n')
	nameObj = Student(,name, g, t, h, pa, pr)


	
##ask to look at directory 
	list_student += [name]
	list_studentObj += [nameObj]   ## NOTE: this is the object. when find_student() is called it will find the index value for the name by a name input. that index (i) will be passed down to find_info(). It will use that index value in list_studentObj  to acces the methods of the class. 
	directory = str(raw_input( 'want to see the list of students? Y/N\n')) 
	if directory == 'Y':
		print (list_student)
		access_dir = raw_input('do you want to access the directory? Y/N\n')
		if access_dir == 'Y':
			access_d()

## funtion to access the directory 
def access_d():
	print list_student,' \n'
	this_student = raw_input ('which student do you want to check?\n')
	find_student(this_student)

##funtion to match  student value in list with the student in question.
def find_student(this_stu):
	global index_for_student
	index_for_student = 0
	which_student = this_stu
	for i in range( len(list_student)):
		if which_student == list_student[i]:
			index_for_student = i
		else:
			pass
	find_info()
##funtion for finding specific atrubutes (methods) for the student in question.
def find_info():
        global index_for_student
        want = raw_input('what do you want to see? 1)all, 2)name, 3)grade, 4)test, 5)hw, 6)participation, 7)project? chose one 1-7.\n' )
        current_student = list_studentObj[index_for_student]
        if want == 'all' or 1:
        	print '\nname: ',current_student.name, '\ngrade: ', current_student.grade, '\ntest: ', current_student.test, '\nhomework: ', current_student.hw, '\nparticipation: ', current_student.participation, '\nproject: ', current_student.project
        pass # for now (code to come later(the code is for the other options))

## actuall program to run. 
keep_going = 'Y'

while keep_going == 'Y' or 'y':
        set_student()
        keep_going = str(raw_input('want to keep going? Y/N\n'))
        if keep_going != 'Y' or 'y':
                break



## to keep the program running
print '\n\n'
is_the_thing_running = raw_input('press enter to exit..' )


'''