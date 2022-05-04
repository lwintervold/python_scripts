import time

from perf import performance_reporter


@performance_reporter
def sleeper():
    time.sleep(1)


if __name__ == '__main__':
    sleeper()
