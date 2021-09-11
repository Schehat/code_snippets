import time


def timing():
    time.sleep(2)
    for _ in range(1000000):
        pass


# timing not including sleep
start = time.process_time()
timing()
end = time.process_time()
# Note: output is around 0.03 although sleep is 2s
print(f"time: {end - start}")


# timing including sleep
start = time.perf_counter()
timing()
end = time.perf_counter()
print(f"time: {end - start}")
