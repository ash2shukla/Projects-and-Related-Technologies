# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import secrets
import string
from random import choice


def generate_random_pass(length):
    choices = string.ascii_letters + string.digits + '!@#$%^&*()'
    return ''.join([choice(choices) for i in range(length)])


def generated_XKCD_pass(length):
    choices = open('/usr/share/dict/words').read().split()
    return ''.join([choice(choices) for i in range(length)])


def get_token_bytes(length):
    return secrets.token_bytes(length)


def main():
    print(get_token_bytes(4))
    print(generated_XKCD_pass(4))
    print(generate_random_pass(4))


if __name__ == "__main__":
    main()
