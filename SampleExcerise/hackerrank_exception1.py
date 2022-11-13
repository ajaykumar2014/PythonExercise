if __name__ == '__main__':
    N = int(input())
    a = []
    for i in range(N):
        a.append(input().split())
    for j in range(len(a)):
        try:
            a1 = a[j][0]
            b1 = a[j][1]
            if not a1.isnumeric(): raise ValueError(f"invalid literal for int() with base 10: '{a1}'")
            if not b1.isnumeric(): raise ValueError(f"invalid literal for int() with base 10: '{b1}'")
            if int(b1) == 0: raise ZeroDivisionError(f'integer division or modulo by zero')
            result: int = int(int(a1) / int(b1))
            print(f'{result}')
        except ValueError as v:
            print(f'Error Code: {v}')
        except ZeroDivisionError as e:
            print(f'Error Code: {e}')
