l=[5, 3, 9, 10, 8, 2, 7]
def find_min(l,current_minimum = None):
    if not l:
        return current_minimum
    candidate=l.pop()
    if current_minimum==None or candidate<current_minimum:
        return find_min(l,candidate)
    return find_min(l,current_minimum)
print find_min(l)
 