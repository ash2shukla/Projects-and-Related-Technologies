from PIL import Image


def read_image_pixels():
    im = Image.open('example_image.jpg')
    print(im.format, im.size, im.mode)
    print(list(im.getdata())[:20])


def write_image_changes():
    im = Image.open('example_image.jpg')
    # show image
    # im.show()
    box = (100, 100, 400, 400)
    # crop a region from image
    region = im.crop(box)
    # region.show()
    region = region.transpose(Image.ROTATE_270)
    # transpose the region cropped
    # region.show()
    r, g, b = im.split()
    # split the channels
    # r.save('filename_to_save.jpg')


if __name__ == '__main__':
    write_image_changes()
