# This program is going to execute fizz buzz

x = range(1, 16)

for thisIter in x:
    isDivBy2 = not(thisIter % 3)
    isDivBy3 = not(thisIter % 5)
    # print('Starting and Iteration for: ' + thisIter.__str__())
    # print('mod 2: ' + isDivBy2.__str__())
    # print('mod 3: ' + isDivBy3.__str__())
    if isDivBy2 and isDivBy3:
        print(thisIter.__str__() + 'fizzBuzz')
    elif isDivBy2:
        print(thisIter.__str__() + 'fizz')
    elif isDivBy3:
        print(thisIter.__str__() + 'buzz')

