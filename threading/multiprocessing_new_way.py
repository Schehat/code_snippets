# multiprocessing on windows is garbage

import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second(s)")
    time.sleep(seconds)
    return f"done sleeping {seconds} seconds(s)"


# need this if for the processing stuff
if __name__ == "__main__":
    # this way is highly recommended than doing start & join manually,
    # especially windows this is the only way to work properly
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [2.5, 2, 1.5]
        # results = [executor.submit(do_something, second) for second in seconds]

        # # for thread in results:
        # #     print(thread.result())

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        results = executor.map(do_something, seconds)

    # if this would have been in the with block it would print the results
    # before the function which is going to be multiprocessed is finished
    # VERY STRANGE
    # Thus always work/print the returns after the with block
    for result in results:
        print(result)

    # need this to be in if to not print this for every process but only 1 time
    finish = time.perf_counter()
    print(f"finished in {finish - start} seconds")
