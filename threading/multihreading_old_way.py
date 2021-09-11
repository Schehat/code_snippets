import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    print("done sleeping")


threads = [threading.Thread(target=do_something, args=[1.5]) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    # like in java wait till threads are completed
    thread.join()

finish = time.perf_counter()

print(f"finished in {finish - start} seconds")
