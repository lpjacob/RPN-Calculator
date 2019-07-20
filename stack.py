"""
Program to demonstrate a stack in Python
by ljacob1@canterbury.kent.sch.uk
Purpose: to demonstrate stack operation, 
Limitations: WIP - not currently fully tested
"""
class Stack:
    """Stack class, allows for a stack like object to be used"""
    def __init__(self, max_height):
        self.__max_height = max_height
        self.__head_pointer = 0
        self.__stack_data = []

    def is_full(self):
        """returns whether the stack is full"""
        if self.__head_pointer < self.__max_height:
            return False
        return True

    def push(self, item):
        """push item on to stack if not full, increments pointer"""
        if not self.is_full():
            self.__stack_data.append(item)
            self.__head_pointer +=1
            print("Stack holds", self.__stack_data)
        else:
            print("stack full")

    def pop(self):
        """returns and removes top item from stack, decrements pointer"""
        removedItem = None #local variable
        if self.__head_pointer >=1:
            self.__head_pointer -=1
            removedItem = self.__stack_data.pop(self.__head_pointer)  
        else:
            print("stack empty")
        return removedItem
