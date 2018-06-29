# -*- coding: UTF-8 -*-
#!/usr/bin/env python3

# For more details see - https://en.wikipedia.org/wiki/ANSI_escape_code
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    print(bcolors.OKBLUE+"My String"+bcolors.ENDC)
    print(bcolors.OKGREEN+"My String"+bcolors.ENDC)
    print(bcolors.WARNING+"My String"+bcolors.ENDC)
    print(bcolors.FAIL+"My String"+bcolors.ENDC)
    print(bcolors.UNDERLINE+"My String"+bcolors.ENDC)
    print(bcolors.BLINK+"My String"+bcolors.ENDC)


if __name__ == "__main__":
    main()
