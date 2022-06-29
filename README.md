# countDistros

these are just python scripts that scrape through [ProtonDB](https://www.protondb.com/) data (published [here](https://github.com/bdefore/protondb-data)), count how many times a distro is reported as being used, and can (optionally) display a pie chart showing the results.

## examples

to view plain text results:
```sh
python countdistros.py reports.json
```

to show a pie chart:
```sh
python countdistros_pichart.py reports.json
```
