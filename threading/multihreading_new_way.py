import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    # print("done sleeping")
    return f"done sleeping {seconds} seconds(s)"


# threads wait at the end of the with statement
# if there is no join inside this block
with concurrent.futures.ThreadPoolExecutor() as executor:
    # pass function & parameter and run thread
    # results contains future objects
    seconds = [2.5, 2, 1.5, 1, 0.5]
    results = [executor.submit(do_something, second) for second in seconds]

    # result() joins all threads
    # for thread in results:
    #     print(thread.result())  # this will return the return statement of the function

    # better way? of returning
    # Note: the first thread which is completed will be printed
    # # different than printing manually
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # results contains the return statements and prints first thread first and so on...
    results = executor.map(do_something, seconds)
    for result in results:
        print(result)

threads = []

finish = time.perf_counter()

print(f"finished in {finish - start} seconds")
