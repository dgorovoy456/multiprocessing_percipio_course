import queue

q = queue.Queue()

print(q.queue)

for i in range(7):
    q.put(i)

print(q.queue)

print(q.empty())

while not q.empty():
    q.get()
    print(q.queue)

print(q.queue)
print(q.empty())

print('##################################')

q = queue.LifoQueue()

for i in range(7):
    q.put(i)

print(q.queue)

print(q.empty())

while not q.empty():
    q.get()
    print(q.queue)

print(q.queue)
print(q.empty())

print('###################################')

q = queue.PriorityQueue()


q.put(5)
q.put(4)
q.put(1)
q.put(3)
q.put(2)
q.put(90)

print(q.queue)

while not q.empty():
    q.get()
    print(q.queue)



