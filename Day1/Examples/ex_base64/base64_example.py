# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import base64


def main():
    byte_string = b'some_data'
    encoded_string = base64.b64encode(byte_string)
    print('The encoded string is', encoded_string)
    decoded_string = base64.b64decode(encoded_string)
    print('The decoded string is', decoded_string)


if __name__ == "__main__":
    main()
