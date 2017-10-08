def calcFee(startTime, endTime):
    
    startHour = float(startTime.split(':')[0])
    endHour = float(endTime.split(':')[0])
    startMinutes = float(startTime.split(':')[1])
    endMinutes = float(endTime.split(':')[1])
    
    time = endHour + endMinutes/60 - (startHour + startMinutes/60)
    fee = 2.5*time
 
    if endHour < 21:
        fee = fee
    elif 21 <= startHour:
        fee = 1.75*time
    else:
        extraHours = endHour - 21
        
        fee = fee - (0.75*(extraHours  + (endMinutes/60)))
 
    return "The babysitters fee is: $%.2f"% fee
 
def main():
    x = raw_input("Using a 24 hour clock, enter the time the sitter arrived: ")
    y = raw_input("Using  a 24 hour clock, enter the time the sitter left: ")
 
    print (calcFee(x,y))
 
main()
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()