class LinkedList:
    def __init__(self, value):
        self.value = value

    def append(self, value):
        self.value = value
    
    def pop(self):
        return self

    def prepend(self, value):
        self.value = value

    def insert(self, index, value);
        self.index = index
        self.value = value
    
    def remove(self, index):
        self.index = index
        