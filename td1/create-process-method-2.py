#!/usr/bin/env python3

from multiprocessing import Process

class Greet(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("Hello,", self.name, "!")

if __name__ == "__main__":
    p = Greet("Kitty")
    p.start()
    p.join()
