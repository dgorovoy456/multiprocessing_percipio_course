import multiprocessing

result = []

num_list = [2, 3, 8]


def square(num):
    global result

    for n in num:
        result.append(n * n)
    print('Child process result: %s' % result)


p1 = multiprocessing.Process(target=square, args=(num_list,))

p1.start()
p1.join()

print('\nMain process result: %s' % result)

print('#############################################')


def square_list(numlist, result, square_sum):
    for idx, num in enumerate(numlist):
        result[idx] = num * num

    square_sum.value = sum(result)


result = multiprocessing.Array('i', 4)

square_sum = multiprocessing.Value('i')

num_list = [1, 2, 3, 4]

p = multiprocessing.Process(target=square_list, args=(num_list,
                                                      result,
                                                      square_sum))

p.start()
p.join()

print(list(result))
print(square_sum.value)
