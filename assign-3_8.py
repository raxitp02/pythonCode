# gcd() function to calculate gcd for the given two numbers
def gcd(a, b):
  
    while b:
        a, b = b, a%b
    return a


while True:
  
    while True:

        
        n1=int(input('\nEnter a positive number '))

       
        if n1==0 or n1 < 0:
            print('Enter a valid positive number greater than zero')
            continue
        else:
            break
  
    while True:

             
        n2=int(input('Enter another positive number '))

        
        if n2==0 or n2 <0:
            print('Enter a valid positive number greater than zero')
            continue
        else:
            break
      
    

    if n1 < n2:
        print('First number should be greater than second number')
        continue

    # calling the gcd function with input arguments
    r=gcd(n1,n2)

    
    print('gcd(%d,%d) is %d \n' %(n1,n2,r))


    

    while True:
      
        choice=input('Do you want to continue? (Yes/Y or No/N) ')

        if choice.lower() == 'yes' or choice.lower()=='y':
            break
        elif choice.lower() == 'no' or choice.lower()=='n':
            break
        else:
            print('Enter an valid character Yes,Y,No,N')
            continue
      
    if choice.lower() == 'yes' or choice.lower()=='y':
            continue
    elif choice.lower() == 'no' or choice.lower()=='n':
            break

