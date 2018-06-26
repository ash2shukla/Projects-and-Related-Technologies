from pickle import load, dump

class X:
    attr = 'x'

def pickle_dump():
    x = X()
    x.attr = 1

    # Let us save this object
    file_pointer = open('X.pkl', 'wb')
    dump(x, file_pointer)
    file_pointer.close()


def pickle_load():
    # load that file
    y = load(open('X.pkl', 'rb'))
    print(y.attr)


if __name__ == "__main__":
    pickle_dump()
    pickle_load()
