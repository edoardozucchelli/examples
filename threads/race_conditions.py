import time
import logging
import threading
import concurrent.futures

from pathlib import Path
from viztracer import VizTracer

from threads.utils import ThreadInfo, timeit


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    @timeit
    def update(self, name):
        thread_info = ThreadInfo()
        logging.info("Thread {}: starting update, value {}".format(thread_info, self.value))

        with self._lock:
            logging.info("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

        logging.info("Thread %s after release", name)
        logging.info("Thread {}: finishing update, value {}".format(name, self.value))


@timeit
def main():
    _format = "%(asctime)s.%(msecs)03d: %(message)s"
    logging.basicConfig(format=_format, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for index in range(3):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)


if __name__ == "__main__":
    out_file = Path(__file__).stem + '.json'
    with VizTracer(output_file=out_file) as tracer:
        main()
