def binSearch(List, items):
	    if len(List) == 0:
	        return False
	    else:
	        midpoint = len(List)//2
	        if List[midpoint]==items:
	          return True
	        else:
	          if items<List[midpoint]:
	            return binSearch(List[:midpoint],items)
	          else:
	            return binSearch(List[midpoint+1:],items)
	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binSearch(testlist, 13))
print(binSearch(testlist, 33))