# multi-processing
# from multiprocess import Process
from multiprocessing import Process
import time


def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print('Finished computing!')


results = {}

processes = [Process(target=longSquare, args=(n, results))
             for n in range(0, 10)]
[p.start() for p in processes]
[p.join() for p in processes]
