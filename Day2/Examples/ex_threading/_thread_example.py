# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
from _thread import start_new_thread


def function_to_run_in_thread():
    for i in range(5):
        print(i)


def main():
    start_new_thread(function_to_run_in_thread, ())
    start_new_thread(function_to_run_in_thread, ())
    while True:
        # Keep waiting so that we can see thread's output
        pass


if __name__ == "__main__":
    main()
