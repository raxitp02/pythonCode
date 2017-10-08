# Use the Stack class to prove that the following HTML tags are valid

class Stack(object) : 
  def __init__(self) : 
    self.items = [] 

  def push(self, item) : 
    self.items.append(item) 

  def pop(self) : 
    return self.items.pop() 

  def isEmpty(self) : 
    return (self.items == [])

  def getStack(self) :
    return self.items

def check_braces(file_data):
    stack = Stack()
    for char in file_data:
        if char == '<':
            stack.push('<')
            #print stack.getStack()
        if char == '>':
            stack.pop()
            #print stack.getStack()
            if stack.isEmpty():
                #print stack.isEmpty()
                return 'braces are valid'
    return 'braces are invalid'

myData = "<!DOCTYPE html><html><body><h2>The title attribute</h2><p title="I'm atooltip">Mouse over this paragraph, to display the title attribute as atooltip.</p></body></html>"

print check_braces(myData)



