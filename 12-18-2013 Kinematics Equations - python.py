# EQN ONE: vf = at + vi
def eq1(vf='n', a='n', t='n', vi='n'):
    '''This funtion is for the equation vf = at + vi. \nEnter the numbers in the order: vf, a, t, vi. \nFor an unkown input \''n'''
    ans = 0
    print "This funtion is for the equation vf = at + vi. \nEnter the numbers in the order: vf, a, t, vi. \nFor an unkown input \'n'"
    if vf == 'n' and a == 'n' and t == 'n' and vi == 'n':   # if no variables are given
        print '\nERROR: you must have 3 knowns and 1 unknown'
    else:
                if vf != 'n' and a != 'n' and t != 'n' and vi != 'n':   # if too many (all) variables are given
                        print '\nERROR: you must have 3 knowns and 1 unknown'
                else:
                        if vf == 'n':   # to solve for final velocity 
                                ans = a*t
                                ans = float (ans) + vi
                                print '\nANSWER: \nThe final velocity is: ', float (ans),'m/s'
                        else:
                                if a == 'n':    # to solve for acceleration
                                        ans = vf - vi
                                        ans = float (ans)/t
                                        print'\nANSWER: \nThe acceleration is: ', float (ans),'m/s^2'
                                else:
                                        if t == 'n':    # to solve for time
                                                ans = vf - vi
                                                ans = abs(float (ans)/a)
                                                print '\nANSWER: \nThe time is: ', float (ans) ,'seconds'
                                        else:
                                                if vi == 'n':   # to solve for initial velocity
                                                        ans = a*t
                                                        ans = vf-float (ans)
                                                        print '\nANSWER: \nThe initial velocity is: ', float (ans),'m/s'


#EQN TWO: DeltaX = 1/2(vf+vi)t

def eq2(Dx='n',vf='n',vi='n',t='n'):
    print Dx




print "pic 'eq1()' or 'eq2()'"
