def oracle():
    guess = 50

    while True:
        print 'Current number = {0}'.format(guess)
        n = raw_input("lower, higher or stop?: ")
        if n == 'stop':
            break
        print "cc"

oracle()