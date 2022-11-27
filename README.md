# Setup

First, install dependencies with `pip install -r requirements.txt`.

Next, you will need to create a .env file in the repo's root directory containing both a CLIENT_ID and CLIENT_SECRET. Follow [this guide](https://developer.spotify.com/documentation/general/guides/authorization/app-settings/) to get these. Your .env file should look something like this:

```
CLIENT_ID=2b3578263588c74b690210ed75b7b71
CLIENT_SECRET=31461804df163a9cdab42680d5abe123
```

# Usage

Once you're all set up, you can run the main script by passing in two artist names as command line arguments. Note that artist names with multiple words will need to be wrapped in quotes. Here's an example:

`py main.py potsu 'Pig Destroyer'`

This script will generate a graph and write it to both a .gml file and .gexf file which you can then open in [Gephi](https://gephi.org/) or other software for analysis.

There are a couple other scripts included which you may also find useful:

`prune.py` will take an existing .gml file built from `main.py` and construct a new graph that only includes the nodes directly neighboring the shortest path between the two artists passed in as command line arguments.

`stats.py` will take an existing .gml file built from `main.py` and output the shortest path between the two artists passed in as command line arguments as well as a chart of the degree distribution on a log-log scale.

Note that you still need to pass in the artist names as command line arguments for these and the artists you pass in must be present in the existing artists.gml file (although not necessarily the same artists passed in when initially running `main.py`). For example:

`py prune.py potsu 'Pig Destroyer'`
