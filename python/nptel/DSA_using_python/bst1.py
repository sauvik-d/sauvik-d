
class Tree:
    def __init__(self, initval = None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    def isempty(self):
        return self.value is None
    def inorder(self):
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder() + [self.value] + self.right.inorder())

    def __str__(self):
        return (str(self.inorder()))
    #lists values in sorted order

    def find(self, v):
        if self.isempty():
            return False
        if self.value == v:
            return True
        if v < self.value:
            return self.left.find(v)
        else:
            return self.right.find(v)

    def minval(self):
        if self.left == None:
            return self.value
        else:
            return self.left.minval()
    def maxval(self):
        if self.right == None:
            return self.value
        else:
            return self.right.minval()
    def insert(self, v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if v < self.value:
            self.left.insert(v)
            return
        if v > self.value:
            self.right.insert(v)
            return

    def isleaf(self):
        if self.left == None and self.right == None:
            return True
        else:
            return False
    def delete(self, v):
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
