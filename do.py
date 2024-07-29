import queue

# Create a priority queue
pq = queue.PriorityQueue()

# Add elements with their priorities to the priority queue
pq.put((5, 'Task 1'))
pq.put((3, 'Task 2'))
pq.put((7, 'Task 3'))

# Dequeue the element with the highest priority
highest_priority_element = pq.get()
print(highest_priority_element)
