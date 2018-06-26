# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
from threading import Thread


class CounterThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(5):
            print(self.name, i)


def main():
    CounterThread("Thread-1").start()
    CounterThread("Thread-2").start()

if __name__ == "__main__":
    main()
