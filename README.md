# Week 5 - Project

## Description
Analyse Deutsche Bahn delays data for 1 year (July 2024 to July 2025).

## Data
Used [Deutsche Bahn Data-Fetching tool](https://github.com/piebro/deutsche-bahn-data) to fetch data from DB's [Timetables API](https://developers.deutschebahn.com/db-api-marketplace/apis/product/timetables), which is under a [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

The .csv file generated with combinedata.py is too big to upload to GitHub. It can be generated locally from a clone of this repo running:
````
python combinedata.py data/datalist.txt combineddata.csv
````

## Questions / Hypothesis
- Are Deustche Bahn trains late more than 33% of the times?
- Is there a difference in train delays between stations in former West/East Germany?
- Is any type of train ("ICE", "IC", "RE", "RB", "S", or "IRE") late more often than others?
- Are trains late more often in a specific season?

## Methodology
### Week plan:
- Monday: 
  - Look for data.
  - Formulate relevant questions.
- Tuesday:
  - Combine dataframes.
  - Filter relevant cities.
  - Clean data.
- Wednesday:
  - Univariate EDA.
  - Bivariate EDA.
- Thursday:
  - Tableau dashboard.
  - Presentation.

### Process:
- functions.py
- clean(df) 
  - Drops columns that aren't needed for this analysis.
  - Resets index.
- filter(df)
  - Filters train types to include only "ICE", "IC", "RE", "RB", "S", and "IRE", which operate only within Germany and are operated by Deustche Bahn.
- group_dates_seasons(df)
  - Creates new columns for "year", "month", "day", and "season".
- separate_cat_num(df)
  - Separates categorical and numerical variables, returning two different dataframes including only those variables.
- group_west_east(df)
  - Adds a new column indicating if the station is within former West or East Germany.

## Conclusions

## Further questions

## Resources
