class Node:
    def __init__(self, initval = None):
        self.value = initval
        self.next = None
    def isempty(self):
        return (self.value == None)

    def append(self, v):
        if self.isempty():
            self.value = v
        elif self.next == None:
            newNode = Node(v)
            self.next =  newNode
        else:
            (self.next).append(v)
        return()

    def insert(self, v):
        if self.isempty():
            self.value = v
            return ()

        newNode = Node(v)
        (self.value, newNode.value) = (newNode.value, self.value)
        (self.next, newNode.next) = (newNode, self.next)
        return ()

    def delete(self, x):
        if self.isempty():
            return ()
        if self.value == x:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return ()
        temp = self
        while temp.next != None:
            if temp.next.value == x:
                temp.next = temp.next.next
                return()
            else:
                temp = temp.next
        return()
    def deleter(self, x):
        if self.isempty():
            return ()
        if self.value == x:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return ()
        else: #recursive delete
            if self.next != None:
                self.next.deleter(x)
            if self.next.value == None:
                self.next = self.next.next
    def __str__(self):
        selflist = []
        if self.value == None:
            return str(selflist)
        temp = self
        selflist.append(temp.value)
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)
        return str(selflist)


l1 = Node()
l2 = Node(8)
print(l1.isempty())
print(l2.isempty())
l1.append(8) # adding at the end of the list
l1.append(7) # adding at the end of the list
l1.append(5) # adding at the end of the list
l1.insert(6) # adding at the start of the list
l1.append(2) # adding at the end of the list
l1.insert(9) # adding at the start of the list
l1.append(4) # adding at the end of the list
l1.delete(6) # deleting the value 6 in the list
print(l1)
