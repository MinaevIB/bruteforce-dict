import hashlib
import itertools
import multiprocessing
import time
import os

time_start = time.time()
hash = 'fbb844c192bb60fc70f5dae33688073f2bbf4656d02fa3bae2402eeeed24b6def9faf6a61e9102c56933f1bd43d588dce64bbf42e3adeceb21c57ee9b4234951'


def brute_force_Process(arg):
    main_chars, sub_chars = arg[0], arg[1]
    alphabet = main_chars + sub_chars
    for letter in itertools.product(alphabet, repeat=6):
        passwd = ''.join(letter)
        if passwd.startswith(sub_chars[0]):
            break
        tmp = hashlib.sha512(passwd.encode()).hexdigest()

        if tmp == hash:
            print(f'password: {passwd}')
            print('Время:', time.time() - time_start)
            break

if __name__ == '__main__':
    with multiprocessing.Pool(processes=16) as pool:
        args = [['0123', '456789abcdefghklmnopqrstuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['4567', '012389abcdefghklmnopqrstuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['89ab', '01234567cdefghklmnopqrstuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['cdef', '0123456789abghklmnopqrstuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['ghkl', '0123456789abcdefmnopqrstuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['mnop', '0123456789abcdefghklqrstuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['qrst', '0123456789abcdefghklmnopuvwxyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['uvwx', '0123456789abcdefghklmnopqrstyzABCDEFGHKLMNOPQRSTUVWXYZ'],
                ['yzAB', '0123456789abcdefghklmnopqrstuvwxCDEFGHKLMNOPQRSTUVWXYZ'],
                ['CDEF', '0123456789abcdefghklmnopqrstuvwxyzABGHKLMNOPQRSTUVWXYZ'],
                ['GHK', '0123456789abcdefghklmnopqrstuvwxyzABCDEFLMNOPQRSTUVWXYZ'],
                ['LMN', '0123456789abcdefghklmnopqrstuvwxyzABCDEFGHKOPQRSTUVWXYZ'],
                ['OPQ', '0123456789abcdefghklmnopqrstuvwxyzABCDEFGHKLMNRSTUVWXYZ'],
                ['RST', '0123456789abcdefghklmnopqrstuvwxyzABCDEFGHKLMNOPQUVWXYZ'],
                ['UVW', '0123456789abcdefghklmnopqrstuvwxyzABCDEFGHKLMNOPQRSTXYZ'],
                ['XYZ', '0123456789abcdefghklmnopqrstuvwxyzABCDEFGHKLMNOPQRSTUVW']]
        result = pool.map(brute_force_Process, args)

