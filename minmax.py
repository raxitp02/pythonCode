def min_max(L, minimum=float('inf'), maximum=-float('inf')):
    
    if not L:
        return minimum, maximum

    if isinstance(L[0], list):
       
        minimum, maximum = min_max(L[0], minimum, maximum)
    else:
        
        minimum = min(minimum, L[0])
        maximum = max(maximum, L[0])

    
    return min_max(L[1:], minimum, maximum)

print(min_max([[3,2,4,6],9,10]))