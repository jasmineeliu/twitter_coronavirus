# Coronavirus twitter analysis

## Overview

This project scans all geotagged tweets sent in 2020 to monitor the spread of coronavirus on social media. To analyze this dataset of about 1.1 billion tweets, this program uses  Python and the MapReduce procedure allowing users to:

-  Extract the total number of tweets associated with chosen hashtags for every day in 2020
- Reduce found totals to return the total number of tweets associated with chosen hashtags for the whole year in 2020
- Group tweets by country or language
- Visualize these results into bar and line plots

With outputted graphs, this program allows users to critically analyze the spread of corona virus by examining what people were tweeting and where.

## File Details
`./src` contains all the Python code for this project. It is broken up into several sections:
- `./src/map.py`, which contains the code for creating a JSON object holding all the tweets with a given hashtag, grouped by language and country
- `./src/reduce.py`, which reduces the given file's counts of hashtags into one larger JSON object 
- `./src/visualize.py`, which takes in hashtag count data and a hashtag and returns a .png file of a barplot with the top 10 groups and how many tweets that group has with the given hashtag
- `./src/alternate_reduce.py`, which plots a line plot for the given days in 2020 and hashtags and returns a .png file of a lineplot with the number of tweets that use that hashtag during the time period. 

Further, in the main folder we have helper files:
- `hashtags`, which contains the list of hashtags we are examining
- `run_maps.sh`, which is a shell script that lets us take all the tweets from 2020 and run our `./src/map.py` code on the data

## Example Plots

Here are a few example plots you could get by running this program:

Using `visualize.py`, you can obtain barplots of with the top 10 countries by number of tweets for the given hashtag:

For `#coronavirus`:
![Barplot showing the Top 10 countries that tweeted #coronavirus in 2020]("./plotoutputs/coronavirus_country.png")

For `#코로나바이러스`:
![Barplot showing the Top 10 countries that tweeted #코로나바이러스 in 2020]("./plotoutputs/coronavirus_korean_country.png")

We can also group by language:

For `#coronavirus`:
![Barplot showing the Top 10 languages that tweeted #coronavirus in 2020]("./plotoutputs/coronavirus_lang.png")

For `#코로나바이러스`:
![Barplot showing the Top 10 languages that tweeted #코로나바이러스 in 2020]("./plotoutputs/coronavirus_korean_lang.png")


Using `alternate_reduce.py`, we can obtain lineplots which demonstrates how usage of hashtags compare between each other and over 2020:

Graph displaying #coronavirus in different languages over 2020:
![Lineplot showing changes in tweets on coronavirus in 2020](./plotoutputs/different_lang_line_plot.png)
 
We can also analyze differences in language and how people referred to the coronavirus online and how this changed over the year:
![Lineplot showing changes in tweets on coronavirus in 2020](./plotoutputs/corona_variations.png)

