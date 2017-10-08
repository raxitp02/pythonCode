def test(): # test function
    nums = list(range(15)) # managing the list
    squareEach(nums) # calling the definition with the data passed
    print(nums) # printing the data
  
def squareEach(nums): # definition of list to squareEach entry
    for counter in range(len(nums)): # iterating over the loop
        nums[counter] **= 2 # updating the values with the square of entry
    return nums # return the list