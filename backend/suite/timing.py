import os
import timeit

def time():
    with open("/app/main.py") as f:
        code = f.read()

    with open("/app/feedback/time.txt", "w") as f:
        f.write("{:.20f}".format(timeit.timeit(code, number=1)))

time()
