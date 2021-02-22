#!/usr/bin/env python3

import sys
import os
#import time
from multiprocessing import Process

def fibonacci(n):
    print(int(os.getpid()))
    res = [0]
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a+b
        res.append(b)
        i += 1
    print(res)
    #time.sleep(10)

if name == "main":
    if len(sys.argv) < 2:
        print("required index argument missing, terminating.", file=sys.stderr)
        sys.exit(1)

    try:
        index = int(sys.argv[1])
    except ValueError:
        print("bad index argument: {}, terminating.".format(sys.argv[1]), file=sys.stderr)
        sys.exit(2)

    if index < 0:
        print("negative index argument: {}, terminating.".format(index), file=sys.stderr)
        sys.exit(3)

    child = Process(target=fibonacci, args=(index,))
    print(int(os.getpid()))
    child.start()
    child.join()