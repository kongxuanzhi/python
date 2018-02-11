__author__ = 'faiyer'
# -*- coding: UTF-8 -*-
import urllib.parse
import urllib.request
import json
import time
import socket
import multiprocessing
import random
import sys
import os
from ctypes import c_char_p
from pymongo import MongoClient
import csv


path = "./csvs"

def requestUrl(file):
    startAt = time.time()
    conn = MongoClient('mongodb://faiyer:123456@localhost:27017/admin')
    db = conn['parkson']
    membercsv = db['membercsv']
    file = os.path.join(path, file)
    print(file)

    with open(file, 'r') as icsvfile:
        spamreader = csv.DictReader(icsvfile)
        rows = []
        for row in spamreader:
            rows.append(row)
            if spamreader.line_num % 1000 == 0:
                membercsv.insert(rows)
                rows = []
                print(spamreader.line_num)
    conn.close()
    endAt = time.time()
    print(file + 'done: ' + str((endAt - startAt)))
    return str((endAt - startAt))

def start():
    pool = multiprocessing.Pool(processes = 50)
    files = multiprocessing.Array(c_char_p, 500)
    files = os.listdir(path)
    result = pool.map(requestUrl, files)

    print("Mark~ Mark~ Mark~~")
    pool.close()
    pool.join()
    for res in result:
        print(":::", res)
    print('get unionIds sub process(es) done.')
    return 'done'

if __name__ == "__main__":
   start()
