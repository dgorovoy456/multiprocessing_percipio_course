import time
import multiprocessing

# def deposit_without_mp(balance, amount):
#     for i in range(100):
#         time.sleep(0.01)
#         balance += amount
#     return balance
#
#
# def withdraw_without_mp(balance, amount):
#     for i in range(100):
#         time.sleep(0.01)
#         balance -= amount
#     return balance
#
#
# balance = 600
#
# balance = deposit_without_mp(balance, 5)
# print(balance)
#
# balance = withdraw_without_mp(balance, 5)
# print(balance)

print('###########################################################')


def deposit_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value += amount
    return balance


def withdraw_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value -= amount
    return balance


balance = multiprocessing.Value('i', 600)

deposit = multiprocessing.Process(target=deposit_without_lock, args=(balance, 5))
withdraw = multiprocessing.Process(target=withdraw_without_lock, args=(balance, 5))

deposit.start()
withdraw.start()

deposit.join()
withdraw.join()

print('Total %d' % balance.value)

print('###########################################################')


def deposit_with_lock(balance, amount, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += amount
        lock.release()


def withdraw_with_lock(balance, amount, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= amount
        lock.release()


lock = multiprocessing.Lock()

balance = multiprocessing.Value('i', 600)

deposit = multiprocessing.Process(target=deposit_without_lock, args=(balance, 5, lock))
withdraw = multiprocessing.Process(target=withdraw_without_lock, args=(balance, 5, lock))

deposit.start()
withdraw.start()

deposit.join()
withdraw.join()

print('Total %d' % balance.value)
