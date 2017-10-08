def squareEach(nums):
    answer = []
    for num in nums:
        answer.append(num*num)
    return answer

def sumList(nums):
    answer = 0
    for num in nums:
        answer += num
    return answer

def toNumbers(strList):
    answer = []
    for numStr in strList.split():
        try:
            num = int(numStr)
            answer.append(num)
        except:
            pass
    return answer

def main():
    print ("** Program to find sum of squares from numbers in a file **")
    fileName = raw_input("What file are the numbers in? ")
    sum = 0
    with open(fileName, 'r') as infile:
        for line in infile:
            nums = toNumbers(line)
            squares = squareEach(nums)
            sum += sumList(squares)
        print (sum)
      