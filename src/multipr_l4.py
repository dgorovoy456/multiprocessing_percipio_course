import time
import multiprocessing
import threading

num_list = [2, 3, 8]


def square(numbers):
    for n in numbers:
        print('square of %d is %d' % (n, n * n))


def cube(numbers):
    for n in numbers:
        print('cube of %d is %d' % (n, n * n * n))


p1 = multiprocessing.Process(target=square, args=(num_list,))
p2 = multiprocessing.Process(target=cube, args=(num_list,))

p1.start()
p2.start()

print(p1.name)
print(p2.name)

p1.join()
p2.join()

print('\nCompleated')

print('######################################################')

square_result = []


def square(numbers):
    global square_result

    for n in numbers:
        print('square for %d is %d' % (n, n * n))
        square_result.append(n * n)


p1 = multiprocessing.Process(target=square, args=(num_list,))

p1.start()
p1.join()

print('\nResult %s' % square_result)

print('\nCompleated')

print('######################################################')

square_result = []


def square(numbers):
    global square_result

    for n in numbers:
        print('square for %d is %d' % (n, n * n))
        square_result.append(n * n)
    print('\nWithin the process, Result %s' % square_result)


p1 = multiprocessing.Process(target=square, args=(num_list,))

p1.start()
p1.join()

print('\nResult %s' % square_result)

print('\nCompleated')

print('######################################################')

square_result = []


def square(numbers):
    global square_result

    for n in numbers:
        print('square for %d is %d' % (n, n * n))
        square_result.append(n * n)
    print('\nWithin the process, Result %s' % square_result)


p1 = threading.Thread(target=square, args=(num_list,))

p1.start()
p1.join()

print('\nResult %s' % square_result)

print('\nCompleated')
