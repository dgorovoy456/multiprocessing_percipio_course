import time
import os
from multiprocessing import Process, current_process

# def square(number):
#     time.sleep(1)
#     result = number * number
#     print('The number %d squares to %d ' % (number, result))
#
#
# numbers = [1, 2, 3, 4]
#
# start_time = time.time()
#
# for i in numbers:
#     square(i)
#
# end_time = time.time()
#
# print('Total time', end_time - start_time)

print('#################################################')

# def square(number):
#     time.sleep(1)
#     result = number * number
#
#     process_id = os.getgid()
#     print('Process ID ', process_id)
#
#     print('The number %d squares to %d ' % (number, result))
#
#
# numbers = [1, 2, 3, 4]
#
# start_time = time.time()
#
# for i, number in enumerate(numbers):
#     process = Process(target=square, args=(number, ))
#     process.start()
#
# process.join()
#
# end_time = time.time()
#
# print('Total time', end_time - start_time)

print('##################################################')


def square(number):
    time.sleep(1)
    result = number * number

    process_id = current_process().pid
    process_name = current_process().name

    print("Process id: {0} \n Process name: {1}".format(process_id, process_name))
    print('The number %d squares to %d' % (number, result))


numbers = [1, 2, 3, 4]

start_time = time.time()

for i, number in enumerate(numbers):
    process = Process(target=square, args=(number,))
    process.start()

process.join()

end_time = time.time()

print('Total time', end_time - start_time)
