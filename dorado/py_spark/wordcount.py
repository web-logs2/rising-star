#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pyspark import SparkConf, SparkContext
from operator import add

if __name__ == '__main__':
    conf = SparkConf().set("spark.driver.host", "127.0.0.1")
    sc = SparkContext("local", "pysparkTest", conf=conf)
    # file_path = sys.argv[1]
    file_path = 'tmp.txt'
    words = sc.textFile(file_path)
    res = words \
        .flatMap(lambda line: line.split(' ')) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(add) \
        .collect()
    for k, v in res:
        print(k, v)
    sc.stop()
