def do_Func(f, value, line):
    i=0 
    while i < line:
        f(value)
        i=i+1

def printer(value):
    print (value)

# Create Grid

rowCell = '|         |         |'
colCell = '+ - - - - + - - - - +'


do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)