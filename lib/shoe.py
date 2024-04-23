#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = None
        
    
    @property
    def size (self):
        return self._size
    
    @size.setter
    def size (self, new_size):
        if type(new_size) == int:
            self._size = new_size
        else:
            print ("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print ("Your shoe is as good as new!")


