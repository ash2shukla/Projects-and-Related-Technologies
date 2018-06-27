# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)


def getset():
    print(r.set('foo', 'bar'))
    print(r.get('foo'))


def main():
    getset()


if __name__ == "__main__":
    main()
