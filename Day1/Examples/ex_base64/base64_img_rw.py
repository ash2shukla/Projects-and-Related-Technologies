# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import base64


def main():
	# We need to read data as binary not text
    image_binary = open('example_image.jpg', 'rb').read()
    encoded_image = base64.b64encode(image_binary)
    print('Binary image is')
    print(image_binary)
    print('Encoded Image is')
    print(encoded_image)

    # Decode the image back to binary
    decoded_image = base64.b64decode(encoded_image)
    print('Decoded Image is')
    print(decoded_image)
    print('Checking if decoded image is what we had given')
    print(decoded_image == image_binary)


if __name__ == "__main__":
    main()
