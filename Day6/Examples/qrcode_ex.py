import qrcode
from io import BytesIO
import base64


def qr_to_image():
    """
    Creates a PNG image of QR corresponding to some_text
    """
    img_obj = qrcode.make('some_text')
    # The argument in save is Byte stream
    # we can open a file in wb mode and give it in
    qr_file = open('qr.png', 'wb')
    img_obj.save(qr_file)


def qr_to_base64():
    """
    Creates a base64 string corresponding to some_text's QR
    """
    img_obj = qrcode.make('some_text')
    qr_stream = BytesIO()
    img_obj.save(qr_stream)
    qr_bytes = qr_stream.getvalue()
    print(qr_bytes)
    print(base64.b64encode(qr_bytes).decode())


if __name__ == "__main__":
    qr_to_image()
    qr_to_base64()
