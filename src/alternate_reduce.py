#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+', required=True)
parser.add_argument('--keys',nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# setting up variables
day = 1
days = []
hashtag_count = [[] for ht in args.keys]
for path in args.input_paths:
    # setting up x axis of days in the year
    days.append(day)
    day += 1

    with open(path) as f:
        tmp = json.load(f)
        for i, ht in enumerate(args.keys):
            # finding the number of tweets per day
            if ht in tmp.keys():
                day_count = (sum(tmp[ht].values()))
            else:
                day_count = 0
            hashtag_count[i].append(day_count)
            
# graphing using matplotlib
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'UnDotum'
matplotlib.rcParams['axes.unicode_minus'] = False

for i, ht in enumerate(args.keys):
    plt.plot(days, hashtag_count[i], label=ht)

plt.xlabel("Days of 2020")
plt.ylabel("Number of Tweets")
plt.title("Days of 2020 vs Number of Tweets with Different #s")
plt.legend()
plt.savefig(args.output_path)


