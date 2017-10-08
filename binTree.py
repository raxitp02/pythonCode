'''

@author: nayeem
'''

class TreeNode():
    def __init__(self,key,leftChild,rightChild,parent):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

class BinSearchTree():
    def __init__(self):
        self.root = None
    
    def returnRoot(self):
        return self.root.key
    
        
    
    def addChild(self,key,Node): 
        if (key < Node.key):
            if (Node.leftChild != None):
                self.addChild(key, Node.leftChild)
            else:
                Node.leftChild = TreeNode(key,None,None,Node)
        else:
            if(Node.rightChild != None):
                self.addChild(key, Node.rightChild)
            else:
                Node.rightChild = TreeNode(key,None,None,Node)
            
    
    def addNode(self,key):
        if self.root == None:
            self.root = TreeNode(key,None,None,None)
        else:
            self.addChild(key,self.root)
            
    def inorderTreeWalk(self,Node):
        if Node != None:
            self.inorderTreeWalk(Node.leftChild)
            print (Node.key)
            self.inorderTreeWalk(Node.rightChild)
            
    def TreeWalk(self,Node):
        if Node != None:
            print (Node.key)
            self.TreeWalk(Node.leftChild)
            self.TreeWalk(Node.rightChild)
    
    def TreeSearch(self,Node,key):
        if (Node == None or key == Node.key):
            return Node
        if key < Node.key:
            return self.TreeSearch(Node.leftChild,key)
        else:
            return self.TreeSearch(Node.rightChild, key)
    
    def TreeMinimum(self,Node):
        while Node.leftChild != None:
            Node = Node.leftChild
        return Node
    
    def TreeMaximum(self,Node):
        while Node.rightChild != None:
            Node = Node.rightChild
        return Node
    
    
    def TreeSuccessor(self,Node):
        if Node.rightChild != None:
            return self.TreeMinimum(Node.rightChild)
        parentNode = Node.parent
        while parentNode != None and Node == parentNode.rightChild:
            Node = parentNode
            parentNode = parentNode.parent
        return parentNode
    
    def TreePredeccessor(self,Node):
        if Node.leftChild != None:
            return self.TreeMaximum(Node.leftChild)
        parentNode = Node.parent
        while parentNode != None and Node == parentNode.leftChild:
            Node = parentNode
            parentNode = parentNode.parent
        return parentNode
    
    def TreeInsert(self,T, Node):
        p = Node.parent
        x = T.root
        while x != None:
            p = x
            if Node.key < x.key:
                x = x.leftChild
            else:
                x = x.rightChild
        Node.parent = p
        if p == None:
            T.root = Node  # Tree was empty
        elif Node.key < p.key:
            p.leftChild = Node
        else:
            p.rightChild = Node
            
            
        
    
        
        
            
        
        
            
        



def main():
    bt = BinSearchTree()
    data = [15,6,18,3,7,17,19]
    for val in data:
        bt.addNode(val)
    print (bt.returnRoot())
    bt.inorderTreeWalk(bt.root)
    print ("*******")
    bt.TreeWalk(bt.root)
    print (bt.TreeMinimum(bt.root).key)
    print (bt.TreeMaximum(bt.root).key)
    
    
    node = bt.TreeSearch(bt.root, 15)
    
    print (bt.TreeSuccessor(node).key)
    
    node = bt.TreeSearch(bt.root, 15)
    print (bt.TreePredeccessor(node).key)
    print ("&&&&&")
    
    tn = TreeNode(8,None,None,None)
    print (bt.TreeInsert(bt, tn))
    bt.inorderTreeWalk(bt.root)
    
    
    
        
if __name__ == "__main__":
    main() 
