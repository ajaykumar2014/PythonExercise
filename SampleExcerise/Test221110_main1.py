#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print('weird')
    if n % 2 == 0 and 2 <= n <= 5:
        print('not weird')
    if n % 2 == 0 and 6 <= n <= 20:
        print('weird')
    if n % 2 == 0 and n > 20:
        print('Not Weird')
