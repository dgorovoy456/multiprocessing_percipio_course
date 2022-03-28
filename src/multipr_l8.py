import multiprocessing


def is_even(numbers, q):
    for n in numbers:
        if n % 2 == 0:
            q.put(n)


def print_numbers(q):
    while not q.empty():
        print(q.get())


q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=is_even, args=(range(10), q))
p2 = multiprocessing.Process(target=print_numbers, args=(q,))

p1.start()
p2.start()

p1.join()
p2.join()

print('###########################################################')


def sender(connection, greets):
    for greet in greets:
        connection.send(greet)
    connection.close()


def receipt(connection):
    while True:
        greet = connection.recv()
        if greet == 'STOP':
            break
        print(greet)


msgs = ['Hello', 'Hola', 'Guten Tag', 'STOP']

sending_pipe, receiving_pipe = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=sender, args=(sending_pipe, msgs))
p2 = multiprocessing.Process(target=receipt, args=(receiving_pipe,))

p1.start()
p2.start()

p1.join()
p2.join()
