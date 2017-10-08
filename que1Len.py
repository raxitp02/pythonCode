def right_justify(rax):
    print ('')
    print ('Total Number of chars are: ' + str(len(rax)))
    print ('')
    print (' '* (70 - len(rax)) + rax)

word = input('Please Enter Any Word: ')
right_justify(word)