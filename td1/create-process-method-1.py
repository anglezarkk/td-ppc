#!/usr/bin/env python3

from multiprocessing import Process

def greet(name):
    print("Hello,", name, "!")

if __name__ == "__main__":
    p = Process(target=greet, args=("Kitty",))
    p.start()
    p.join()
