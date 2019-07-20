"""
Program to perform demonstrate a static queue in Python
by ljacob1@canterbury.kent.sch.uk
Purpose: to demonstrate queue operation, 
Limitations: WIP - not currently fully tested
"""

class Queue:
    """Queue class, allows for a queue like object to be used"""
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__queue_data = []
        self.__tail_pointer = 0

    def queue_Size(self):
        """Returns the current queue size"""
        return len(self.__queue_data)

    def is_empty(self):
        """Returns whether the queue is empty"""
        if len(self.__queue_data) > 0:
            return False
        return True

    def enqueue(self, item):
        """Adds an item into the queue"""
        if self.__tail_pointer < self.__max_size:
            self.__queue_data.append(item)
            print("queue containts", self.__queue_data)
        else:
            print("queue full")

    def dequeue(self):
        """Removes an item from the queue, returns None if empty"""
        removedItem = None
        if not self.is_empty():
            removedItem = self.__queue_data.pop(0)
            print("queue containts", self.__queue_data)
        else:
            print("Queue Empty!")
        return removedItem

if __name__ =="__main__":
    queue = Queue(5)
    queue.enqueue("+")
    queue.enqueue("*")
    print(queue.dequeue())
    queue.enqueue("-")
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
