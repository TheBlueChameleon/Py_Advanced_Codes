# ============================================================================ #
# linked list iterable code
# in this, we added the LinkedListIterable class, allowing to traverse the list
# in a for loop

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
    
    # ........................................................................ #
    
    def __iter__ (self) :
        return LinkedListIterable(self.first)
    
# ---------------------------------------------------------------------------- #

class LinkedListElement :
    def __init__ (self, realData, nextNode = None) :
        self.realData = realData
        self.nextNode = nextNode

# ---------------------------------------------------------------------------- #

class LinkedListIterable :
    def __init__ (self, current) :
        self.current = current
    
    # ........................................................................ #
    
    def __iter__ (self) :
        # this allows to manually skip items before or in a for loop.
        # consider this scenario:
        # 
        # iterObj = iter(myList)
        # next(iterObj)             # skip the first object
        # for line in iterObj :     # for calls __iter__ on iterObj, which simply returns self
        #     pass                  # so, the previous next(iterObj) affects the loop -- the first element has really been skipped!
        
        return self
    
    # ........................................................................ #
    
    def __next__ (self) :
        if self.current :
            reVal = self.current.realData
            self.current = self.current.nextNode
            return reVal
        else :
            raise StopIteration()
    
# ============================================================================ #

myList = LinkedList()                                                           # create an empty list

myList.push("!")                                                                # fill with some content
myList.push("flow")
myList.push("must")
myList.push("Spice")
myList.push("The")

# automated output
for line in myList :
    print(line)

print()

# just some shenanigans, to realize the mechanics at play
for line in myList :                                                            # this creates a first instance of LinkedListIterable ...
    print(line)
    for word in myList :                                                        # ... and this creates a second instance. They both have their own, independent .current attribute.
        print("", word, end="")
    print()
