from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'hola'))
q.put((1, 'adiós'))
q.put((3, 'qué tal'))

print(q.get())

print(q.empty())

print(q.peek())

print(len(q))

print(list(q))