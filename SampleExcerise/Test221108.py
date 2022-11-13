import time

print(time.time())
print(time.localtime())


def my_timer(func):
    def _timer(*args, **kwargs):
        start = time.time();
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Execution Time {end - start}')
        return result

    return _timer;


@my_timer
def delayed_mean(sample):
    time.sleep(1)
    return sum(sample) / len(sample)


delayed_mean([10, 2, 4, 7, 9, 3, 9, 8, 6, 7])


def power_factory(exp):
    def power(number):
        return exp ** number

    return power


print(f'factorial is {power_factory(2)(3)}')
