# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import yaml
import sys
class X:
    pass


def load_yaml():
    file_pointer = open('Sample_YAML.yml')
    print(yaml.load(file_pointer.read()))


def dump_yaml():
    # Yaml can dump virtually any python object 
    # but it is advisable to dump only the builtins 
    print(yaml.dump(X()))
    print(yaml.dump([1,2,3]))

def main():
    dump_yaml()


if __name__ == "__main__":
    main()
