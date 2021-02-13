# ============================================================================ #
# linked list basic code
# this implements the basic data structure of a linked list
# traversing the list is done manually here.

class LinkedList :
    def __init__ (self, data = None) :
        
        if data :
            self.first = LinkedListElement()
            self.N = 1
        else :
            self.first = None
            self.N = 0
    
    # ........................................................................ #
    
    def push (self, data) :                                                     # insert on top of the stack
        self.first = LinkedListElement(data, self.first)
        self.N += 1
    
    # ........................................................................ #
    
    def pop (self) :                                                            # remove and return the first element on the stack
        if self.N == 0 :
            raise RuntimeError("Attempt to remove from empty list!")
        
        reVal = self.first.realData
        
        self.first = self.first.nextNode
        
        return reVal
    
    # ........................................................................ #
    
    def indexCheck (self, index) :
        if type(index) != int :
            raise TypeError("Index has to be int!")
        
        if not (0 <= index < self.N) :
            raise IndexError("Index out of bounds!")
    
    # ........................................................................ #
    
    def __getitem__ (self, index) :                                             # allow (slow) random read access like print( myList[5] )
        self.indexCheck(index)
        
        current = self.first
        for i in range(index) :
            current = current.nextNode
        
        return current.realData
    
    # ........................................................................ #
    
    def __setitem__ (self, index, value) :                                      # allow (slow) random write access like myList[5] = "Sir Robin bravely ran away"
        self.indexCheck(index)
        
        current = self.first
        for i in range(index) :
            current = current.nextNode
        
        current.realData = value
    
# ---------------------------------------------------------------------------- #

class LinkedListElement :
    def __init__ (self, realData, nextNode = None) :
        self.realData = realData
        self.nextNode = nextNode

# ============================================================================ #

myList = LinkedList()                                                           # create an empty list

# fill with some content
myList.push("!")                                                                # recall that we designed a FIFO
myList.push("flow")                                                             # thus, our strings are in
myList.push("must")                                                             # reverse order
myList.push("Spice")
myList.push("The")

# manual output on screen
current = myList.first
while current :
    print(current.realData)
    current = current.nextNode
