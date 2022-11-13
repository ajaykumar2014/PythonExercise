#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    for x in range(1, n + 1):
        print(f'{x} ', end='')

    a = '1'
    b = '0'
    try:
        print(int(a) / int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
