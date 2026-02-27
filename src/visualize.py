#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--output_png',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# getting the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_10 = []
top_10_values = []
i = 0
for k,v in items:
    top_10.append(k)
    top_10_values.append(v)
    i += 1
    if i == 10:
        break

#plotting
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

ax.bar(top_10, top_10_values, width=1, edgecolor="white", linewidth=0.7)
plt.savefig(args.output_png)

plt.show()
