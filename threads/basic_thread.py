import threading
import time

from viztracer import VizTracer
from pathlib import Path

from threads.utils import ThreadInfo, timeit


@timeit
def thread_func(name):
    print('thread {}: starting'.format(name))

    thread_info = ThreadInfo()
    print(thread_info)

    time.sleep(2)

    print('thread {}: finishing'.format(name))


@timeit
def main():
    print("Main    : before creating thread")
    x = threading.Thread(target=thread_func, args=(1,), daemon=True)
    print("Main    : before running thread")
    x.start()
    print("Main    : wait for the thread to finish")
    x.join()
    print("Main    : all done")


if __name__ == '__main__':
    out_file = Path(__file__).stem + '.json'
    with VizTracer(output_file=out_file) as tracer:
        main()
