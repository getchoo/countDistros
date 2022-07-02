#!/usr/bin/env python
import json
from multiprocessing import Manager, Process
import re
import sys

# array of distro names (EDIT THIS AND PROBABLY USE CAPITALIZATION)
arr = ['Ubuntu', 'Linux Mint', 'Pop!_OS', 'Debian', 'Arch Linux',
       'Manjaro Linux', 'Fedora']


def get_count(distro, db, data):
    # print how many times distro appears in report
    # by matching its' name to data using regex
    rg = re.compile(distro)
    count = 0
    for item in db:
        if re.search(rg, item['systemInfo']['os']):
            count += 1
    data[distro] = str(count)


def get_data(filename='reports_piiremoved.json'):
    # use default file name if file is not supplied
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print('defaulting to ' + filename + ' since no argument was supplied')

    # try to load file as json
    db = None
    try:
        with open(filename) as file:
            db = json.load(file)
    except Exception:
        err = filename + ' doesn\'t exist or isn\'t valid json!'
        print(err)
        sys.exit(1)

    # get distro count asynchronously :trollfig:
    data = Manager().dict()
    procs = []
    for distro in arr:
        proc = Process(target=get_count, args=(distro, db, data))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    return data


def print_data():
    data = get_data()
    for key in data:
        print(key + ': ' + data[key])


if __name__ == "__main__":
    print_data()
