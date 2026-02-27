#!/bin/sh

for i in /data/Twitter\ dataset/geoTwitter20*
do
    filename=$(basename "$i")
    nohup python3 -u src/map.py --input_path="$i" > "logs/$filename.log" 2>&1 &
done
