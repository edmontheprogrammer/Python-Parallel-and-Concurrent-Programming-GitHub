# multi-threading

# Threading:
# Emulates parallel computing
# Useful when your programs have periods of downtime

import threading
import time


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2


results = {}

threads = [threading.Thread(target=longSquare, args=(n, results))
           for n in range(0, 100)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)
