__author__ = 'meramac'
import asyncio
import sys
from time import time

def fib(n):
    if n <= 1:
        yield n
    else:
        a = yield fib(n - 1)
        b = yield fib(n - 2)
        yield a + b

def process_input():
    text = sys.stdin.readline()
    n = int(text.strip())
    print('fib({}) = {}'.format(n, fib(n)))


@asyncio.coroutine
def print_hello():
    while True:
        print("{} - Hello world!".format(int(time())))
        yield from asyncio.sleep(3)


def main():
    loop = asyncio.get_event_loop()
    loop.add_reader(sys.stdin, process_input)
    loop.run_until_complete(print_hello())


if __name__ == '__main__':
    main()