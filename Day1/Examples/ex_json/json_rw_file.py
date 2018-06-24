# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import json
from pprint import pprint


def main():
    file_pointer = open('file.json')
    # Mind that function is load not loads
    loaded_json = json.load(file_pointer)
    print('The loaded file is')
    pprint(loaded_json)

    write_file_pointer = open('new_file.json', 'w')
    print('Dumping the loaded file to new_file.json')
    # Mind that function is dump not dumps
    json.dump(loaded_json, write_file_pointer)
    print('File Dumped')


if __name__ == "__main__":
    main()
