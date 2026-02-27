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
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)[:10]
top_10 = []
top_10_values = []
top_items = sorted(items, key=lambda item: item[1])
for k,v in top_items:
    top_10.append(k)
    top_10_values.append(v)
print(top_10)
print(top_10_values)

#plotting
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
matplotlib.rcParams['font.family'] = 'UnDotum'
matplotlib.rcParams['axes.unicode_minus'] = False
if 'lang' in args.input_path:
    file_type = "Language"
else:
    file_type = "Country"

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm

for font in fm.findSystemFonts():
    print(font)
plt.bar(top_10, top_10_values, width=1, edgecolor="white", linewidth=0.7)
plt.title("Tweets with " + args.key + " by " + file_type)
plt.ylabel("Number of tweets")
plt.xlabel(file_type)
plt.savefig(args.output_png)

plt.show()
