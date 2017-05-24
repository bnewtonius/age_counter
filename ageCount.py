#!/usr/bin/env python
import sys
import csv

def increment(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
    return d

def getTuples(csvFile):
    with open(csvFile) as f:
        data=[tuple(line) for line in csv.reader(f)]
    return data

def getCounts(data):
    reduced = reduce(lambda output, current: increment(output, current[1]), data, {})
    return "\n".join(["{},{}".format(k, v) for k,v in reduced.items()])

def main(args):
    if ( len(args) < 1 ):
        print "Please provide a csv file"
        sys.exit(1)

    csvFile = args[0]

    data = getTuples(csvFile)
    counts = getCounts(data)
    print counts

if __name__ == "__main__":
    main(sys.argv[1:])
