def is_triangle(x,y,z):
    if(z>(x+y)):
        print ("False")
    elif(y>(x+z)):
        print ("False")
    elif(x>(z+y)):
        print ("False")
    else:
        print ("True")
        
is_triangle(3,4,5)
is_triangle(1,2,4)
is_triangle(9,4,4)
