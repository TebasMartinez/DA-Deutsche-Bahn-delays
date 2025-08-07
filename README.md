# Data Analysis - Deutsche Bahn delays

## Description
Analyse Deutsche Bahn delays data for 1 year (July 2024 to July 2025) including Regional and Intercity trains ICE, IC, RE, RB, and IRE.

## Data
Used [Deutsche Bahn Data-Fetching tool](https://github.com/piebro/deutsche-bahn-data) to fetch data from DB's [Timetables API](https://developers.deutschebahn.com/db-api-marketplace/apis/product/timetables), which is under a [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

The file `data/combineddata.csv`, used in the Jupyter Notebooks throughout the analysis, is too big to upload to GitHub. It can be generated locally from a clone of this repo running `combinedata.py`:
````
python combinedata.py data/datalist.txt combineddata.csv
````

The file `data/clean_grouped_combineddata.csv`, used in Tableau, is also too big to upload to GitHub. Once `data/combineddata.csv` has been created with the previous command, it can be generated locally from a clone of this repo running `clean_filter_group_data.py`:
````
python clean_filter_group_data.py
````

## Questions / Hypothesis
- Are Deutsche Bahn trains late more than 33% of the times?
- Is there a difference in train delays between stations in former West/East Germany?
- Is any type of train (ICE, IC, RE, RB, or IRE) late more often than others?
- Are trains late more often in a specific season?

## Methodology
### Week plan:
- Monday: 
  - Look for data.
  - Formulate relevant questions.
- Tuesday:
  - Combine dataframes.
  - Filter data.
  - Clean data.
- Wednesday:
  - Univariate EDA.
  - Bivariate EDA.
- Thursday:
  - Tableau dashboard.
  - Presentation.

### Punctuality definition:
- For this analysis, I've used the same definition of punctuality that the Deutsche Bahn considers in [their own reports](https://www.deutschebahn.com/de/konzern/konzernprofil/zahlen_fakten/puenktlichkeitswerte-6878476#). Trains are considered on time if they arrive less than 6 minutes late.

### Train types included:
- ICE: InterCityExpress
- IC: InterCity
- RE: Regional-Express
- RB: Regionalbahn
- IRE: Interregio-Express

### Process:
- `functions.py`
  - clean(df) 
    - Drops columns that aren't needed for this analysis.
    - Resets index.
  - filter(df)
    - Filters train types to include only "ICE", "IC", "RE", "RB", and "IRE".
  - group_dates_seasons(df)
    - Creates new columns for "year", "month", "day", and "season", and assigns relevant values to each row.
  - group_puctuality(df)
    - Creates new column "punctuality" and assigns relevant values to each row: "On time", "Late", "Early", "Canceled".
  - separate_cat_num(df)
    - Separates categorical and numerical variables, returning two different dataframes including only those variables.
  - group_west_east(df)
    - Adds a new column indicating if the station is within former West or East Germany. For the purposes of this analysis, all stations in Berlin have been labelled as East.

## Conclusions

[Tableau dashboard](https://public.tableau.com/views/DA-Deutsche-Bahn-delays/DA-DeutscheBahndelays)

## Further questions

## Resources

<div class='tableauPlaceholder' id='viz1754579244876' style='position: relative'><noscript><a href='#'><img alt='DA - Deutsche Bahn delays ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DA&#47;DA-Deutsche-Bahn-delays&#47;DA-DeutscheBahndelays&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DA-Deutsche-Bahn-delays&#47;DA-DeutscheBahndelays' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DA&#47;DA-Deutsche-Bahn-delays&#47;DA-DeutscheBahndelays&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1754579244876');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='1416px';vizElement.style.height='991px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
