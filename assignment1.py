rom pythonds.basic.stack import Stack

def divBy2(decNum):
    remstack = Stack()

    while decNum > 0:
        rem = decNum % 2
        remstack.push(rem)
        decNum = decNum // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divBy2(36))