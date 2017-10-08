#sumList(nums)method: The variable "nums" is a list of numbers.
#This method returns the sum of the numbers in the list.      
def sumList(nums):
    sum = 0
    for number in nums:
        sum += number
    return(sum)

#main method for call the function,"sumList" and
#display output
def main():
    print("The list of numbers:",[10,40,50,9,11])
    print("The sum of the numbers in the list:",sumList([10,40,50,9,11]))
main()