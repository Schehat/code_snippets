# multiprocessing on windows is garbage

import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("done sleeping")


# this if statement is necessary in windows
# Note: in windows the code does run parallel but they are finished in order
# e.g. take a closer look at the output
# This way of doing multiprocessing is highly unrecommended, especially on windows
if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=do_something, args=[1]) for _ in range(4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    finish = time.perf_counter()
    print(f"finished in {finish - start} seconds")
