#!/usr/bin/env python3

class Book:
    def __init__(self, title:str, page_count):
        self.title = title
        self._page_count = page_count #why _here?

        
    @property #getting the value
    def page_count(self):
        return self._page_count
   
    @page_count.setter
    def page_count(self, value):
        if type(value) != int:
            # self.page_count = "not an integer"
            print ("page_count must be an integer") 
        else:
            self._page_count = value


    def turn_page(self):
        print ("Flipping the page...wow, you read fast!")
        # print ("Flipping the page...wow, you read fast!")