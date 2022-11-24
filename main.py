import hashlib
import itertools
import multiprocessing
import time
import os

time_start = time.time()
hash = '569e6e1b98165fbda0f88aba58e7741b27091393'
def brute_force_Process(arg):
    main_chars, sub_chars = arg[0], arg[1]
    alphabet = main_chars + sub_chars
    for letter in itertools.product(alphabet, repeat=6):
        passwd = ''.join(letter)
        if passwd.startswith(sub_chars[0]):
            break
        tmp = hashlib.sha1(passwd.encode()).hexdigest()

        if tmp == hash:
            print(f'password: {passwd}')
            break
if __name__ == '__main__':
    with multiprocessing.Pool(processes=16) as pool:
        args = [['0123', '456789abcdefg'],
                ['4567', '012389abcdefg'],
                ['89ab', '01234567cdefg'],
                ['cdefg', '0123456789ab']]
        result = pool.map(brute_force_Process, args)
    print('Время:', time.time() - time_start)