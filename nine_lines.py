def new_line():
    print('.\n')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clearScreen():
    print('Printing nine lines')
    nine_lines()
    print('Printing three lines')
    three_lines()
    print('Printing three lines')
    three_lines()
    print('Printing new line')
    new_line()

nine_lines()
clearScreen()
