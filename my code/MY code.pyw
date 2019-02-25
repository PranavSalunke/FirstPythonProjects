# Eng to code

def EtoC(): 
    x = 1
    list1 = []
    list2 = []
    a = raw_input ('What do you want to translate to Code? Input must in in lower case. \n')
    le = len(a)
    for i in range(0,le,1):
        list1 += a[i]
    print 'This was your original string: \n',list1
    for i in range(0,le,1):
        if list1[i] == 'a':
            list2 += ['k']
        if list1[i] == 'b':
            list2 += ['j']
        if list1[i] == 'c':
            list2 += ['b']
        if list1[i] == 'd':
            list2 += ['!']
        if list1[i] == 'e':
            list2 += ['d']
        if list1[i] == 'f':
            list2 += ['a']
        if list1[i] == 'g':
            list2 += ['2']
        if list1[i] == 'h':
            list2 += ['e']
        if list1[i] == 'i':
            list2 += ['f']
        if list1[i] == 'j':
            list2 += ['$']
        if list1[i] == 'k':
            list2 += ['g']
        if list1[i] == 'l':
            list2 += ['7']
        if list1[i] == 'm':
            list2 += ['h']
        if list1[i] == 'n':
            list2 += ['*']
        if list1[i] == 'o':
            list2 += ['i']
        if list1[i] == 'p':
            list2 += [':']
        if list1[i] == 'q':
            list2 += ['#']
        if list1[i] == 'r':
            list2 += ['c']
        if list1[i] == 's':
            list2 += ['9']
        if list1[i] == 't':
            list2 += ['@']
        if list1[i] == 'u':
            list2 += ['>']
        if list1[i] == 'v':
            list2 += ['m']
        if list1[i] == 'w':
            list2 += ['n']
        if list1[i] == 'x':
            list2 += ['4']
        if list1[i] == 'y':
            list2 += ['p']
        if list1[i] == 'z':
            list2 += ['q']
        if list1[i] == ' ':
            list2 += [' ']
        if list1[i] == '!':
            list2 += ['(i)']
        if list1[i] == '.':
            list2 += ['(...)']
        if list1[i] == ',':
            list2 += ['(\')']
        if list1[i] == '?':
            list2 += ['(Qu.)']
    print '\nHere is your new one! As Code \n', list2



# code to Eng. 

def CtoE():
    x = 1
    list1 = []
    list2 = []
    a = raw_input ('What do you want to translate to English? Input must in in lower case. \n')
    le = len(a)
    for i in range(0,le,1):
        list1 += a[i]
    print 'This was your original code: \n',list1
    for i in range(0,le,1):
        if list1[i] == 'k':
            list2 += ['a']
        if list1[i] == 'j':
            list2 += ['b']
        if list1[i] == 'b':
            list2 += ['c']
        if list1[i] == '!':
            list2 += ['d']
        if list1[i] == 'd':
            list2 += ['e']
        if list1[i] == 'a':
            list2 += ['f']
        if list1[i] == '2':
            list2 += ['g']
        if list1[i] == 'e':
            list2 += ['h']
        if list1[i] == 'f':
            list2 += ['i']
        if list1[i] == '$':
            list2 += ['j']
        if list1[i] == 'g':
            list2 += ['k']
        if list1[i] == '7':
            list2 += ['l']
        if list1[i] == 'h':
            list2 += ['m']
        if list1[i] == '*':
            list2 += ['n']
        if list1[i] == 'i':
            list2 += ['o']
        if list1[i] == ':':
            list2 += ['p']
        if list1[i] == '#':
            list2 += ['q']
        if list1[i] == 'c':
            list2 += ['r']
        if list1[i] == '9':
            list2 += ['s']
        if list1[i] == '@':
            list2 += ['t']
        if list1[i] == '>':
            list2 += ['u']
        if list1[i] == 'm':
            list2 += ['v']
        if list1[i] == 'n':
            list2 += ['w']
        if list1[i] == '4':
            list2 += ['x']
        if list1[i] == 'p':
            list2 += ['y']
        if list1[i] == 'q':
            list2 += ['z']
        if list1[i] == ' ':
            list2 += [' ']
        if list1[i] == '(i)':
            list2 += ['!']
        if list1[i] == '(...)':
            list2 += ['.']
        if list1[i] == '(\')':
            list2 += [',']
        if list1[i] == '(Qu.)':
            list2 += ['?']
    print '\nHere is your new one! As regular! \n', list2


keep_going = 'y'

while keep_going == 'y':
    
    EtoC()
    CtoE()
    keep_going = raw_input('Want to go again? Y/N \n')
    if keep_going == 'n' or 'N':
        print ('ending')
    else:
        print ('-----------------------')



