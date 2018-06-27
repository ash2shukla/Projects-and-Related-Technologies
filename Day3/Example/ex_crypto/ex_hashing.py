# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import hashlib
import hmac


def hashes():
    string = b'string_to_hash'
    print(hashlib.sha256(string).hexdigest())

    content = open('sample.wav', 'rb').read()
    print(hashlib.md5(content).hexdigest())


def hmacs():
    string = b'string_to_hash'
    shared_key = b'my_key'
    print(hmac.new(shared_key, string).hexdigest())


def main():
    hashes()


if __name__ == "__main__":
    main()
