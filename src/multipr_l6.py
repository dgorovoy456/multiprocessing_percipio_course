import multiprocessing


def get_data(data_list):
    for data in data_list:
        print('Name: %s \nScore: %d\n' % (data[0], data[1]))


def append(new_data, data_list):
    data_list.append(new_data)
    print('New data appended!\n')


database = ([('Maura', 70), ('Alexis', 79), ('Pete', 96)])
database1 = (('Maura', 70), ('Alexis', 79), ('Pete', 96))
new_data = ('Leroy', 87)

p1 = multiprocessing.Process(target=append, args=(new_data, database))

p2 = multiprocessing.Process(target=get_data, args=(database,))

p1.start()
p1.join()

p2.start()
p2.join()

print(database)

print('#############################################################')

with multiprocessing.Manager() as manager:
    database = (manager.list([('Maura', 70), ('Alexis', 79), ('Pete', 96)]))
    new_data = ('Leroy', 87)

    p1 = multiprocessing.Process(target=append, args=(new_data, database))
    p2 = multiprocessing.Process(target=get_data, args=(database,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Data available to the Manager: ', database)
