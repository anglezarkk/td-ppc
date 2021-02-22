#!/usr/bin/env python3

import os
import sys
import time
import signal
from multiprocessing import Process

def handler(sig, frame):
    if sig == signal.SIGUSR1:
        os.kill(childPID, signal.SIGKILL)
        print("Die, son!")

def child():
    time.sleep(5)
    os.kill(os.getppid(), signal.SIGUSR1)
    while True:
        print("Get up dad!")

if __name__ == "__main__":
    signal.signal(signal.SIGUSR1, handler)

    childProcess = Process(target=child, args=())
    childProcess.start()
    global childPID
    childPID = childProcess.PID
    childProcess.join()