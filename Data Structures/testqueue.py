from lab9pr1 import *


queue = Queue()
print ("Queue now:", queue)
print ("isEmpty?", queue.isEmpty())
print ("Enqueuing a")
queue.enqueue('a')
print ("Queue now:", queue)
print ("Enqueuing b")
queue.enqueue('b')
print ("isEmpty?", queue.isEmpty())
print ("Queue now:", queue)
print ("Enqueuing c")
queue.enqueue('c')
print ("Queue now:", queue)
print ("Dequeued:", queue.dequeue())
print ("Queue now:", queue)
print ("Dequeued:", queue.dequeue())
print ("Queue now:", queue)
print ("Enqueuing d")
queue.enqueue('d')
print ("Queue now:", queue)
print ("Enqueuing e")
queue.enqueue('e')
print ("Queue now:", queue)
print ("Dequeued:", queue.dequeue())
print ("Queue now:", queue)
print ("Dequeued:", queue.dequeue())
print ("Queue now:", queue)
print ("Dequeued:", queue.dequeue())
print ("Queue now:", queue)
print ("isEmpty?", queue.isEmpty())
        
        
