"""
    Olanrewaju Ojebisi
    Ojebisicuit1@yahoo.com
"""


from math import sqrt
print ('welcome to pythagoras theorem calculator! Calculate your triangle sides here!')
formula = input('which side do you wish to calculate? side _ _ _ _')

if formula == 'c':
    sidea = input('what is the length of side a?')
    sideb = input('what is the length of side b?')

    sidea = int(sidea)
    sideb = int(sideb)

    answercsquared = sidea * sidea + sideb * sideb
    answerc = sqrt(answercsquared)

    print ('The length of side c is')
    print (answerc)

elif formula == 'a':
    sideb = input('what is the length of side b?')
    sidec = input('what is the length of side c?')

    sideb = int(sideb)
    sidec = int(sidec)

    answerasquared = (sidec * sidec) - (sideb * sideb)
    answera = sqrt(answerasquared)

    print ('The length of side a is')
    print (answera)

elif formula == 'b':
    sidea = input('What is the length of side a?')
    sidec = input('What is the length of side c?')

    sidea = int(sidea)
    sidec = int(sidec)

    answerbsquared = (sidec) * sidec - (sidea * sidea)
    answerb = sqrt(answerbsquared)
    print ('The length of side b is')
    print (answerb)

else:
        print ('please select the formular')
