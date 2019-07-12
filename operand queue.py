"""
Program to demonstrate a static queue in Python
by ljacob1@canterbury.kent.sch.uk
Purpose: to demonstrate queue operation, 
Limitations: WIP - not currently fully tested
"""

"""global variables"""
queue = []
maxSize = 5 #constant to set max queue size
tailPointer = 0

    

def enqueue(item):
    """add an item to the tail of the queue if its not full"""
    global queue, maxSize, tailPointer
    if tailPointer < maxSize:
        queue.append(item)
        tailPointer 
        print("queue containts", queue)
    else:
        print("queue full")
   

def dequeue():
    global queue, maxSize, headPointer, tailPointer
    removedItem = None
    if len(queue)>0:
        removedItem = queue.pop(0)
        print("queue containts", queue)
    else:
        print("Queue Empty!")
    return removedItem

if __name__ =="__main__":

    enqueue("+")
    enqueue("*")
    print(dequeue())
    enqueue("-")
    print(dequeue())
    print(dequeue())
    print(dequeue())
        
