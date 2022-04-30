#!/usr/bin/python3
"""
Python script takes URL from stdin and compute exact metrics
"""


def printst(dictionary, size):
    """
    Print function
    """
    d = sorted(dictionary.keys())
    print("File size: {:d}".format(size))
    for i in d:
        if dictionary[i] != 0:
            print("{}: {:d}".format(i, dictionary[i]))

count = 0
size = 0
dic = {"200": 0, "301": 0, "400": 0, "401": 0,
       "403": 0, "404": 0, "405": 0, "500": 0}

try:
    with open(0) as f:
        for line in f:
            count += 1
            arr = line.split()
            try:
                size += int(arr[-1])
            except:
                pass
            try:
                st = arr[-2]
                if st in dic:
                    dic[st] += 1
            except:
                pass
            if count % 10 == 0:
                printst(dic, size)
        printst(dic, size)

except KeyboardInterrupt:
    printst(dic, size)
    raise
