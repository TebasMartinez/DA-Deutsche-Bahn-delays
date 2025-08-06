import pandas as pd

def filter(df):
    df = df[df["train_type"].isin(["ICE", "IC", "RE", "RB", "IRE"])]
    return df

def clean(df):
    notneeded_columns = [
        "arrival_planned_time", 
        "arrival_change_time", 
        "departure_planned_time", 
        "departure_change_time", 
        "train_line_station_num"]
    df = df.drop(columns=notneeded_columns)
    df.reset_index(drop=True, inplace=True)
    return df

def group_dates_seasons(df):
    df["year"] = pd.DatetimeIndex(df["time"]).year
    df["month"] = pd.DatetimeIndex(df["time"]).month
    df["day"] = pd.DatetimeIndex(df["time"]).day
    df.loc[df["month"].isin([3,4,5]), "season"] = "Spring"
    df.loc[df["month"].isin([6,7,8]), "season"] = "Summer"
    df.loc[df["month"].isin([9,10,11]), "season"] = "Autumn"
    df.loc[df["month"].isin([12,1,2]), "season"] = "Winter"
    return df

def group_puctuality(df):
    df.loc[(df["delay_in_min"] > 5) & (df["is_canceled"] == False), "punctuality"] = "Late"
    df.loc[(df["delay_in_min"] < 0) & (df["is_canceled"] == False), "punctuality"] = "Early"
    df.loc[(df["delay_in_min"] >= 0) & (df["delay_in_min"] < 6) & (df["is_canceled"] == False), "punctuality"] = "On time"
    df.loc[df["is_canceled"] == True, "punctuality"] = "Canceled"
    return df

def separate_cat_num(df):
    categorical_from_numerical = df.select_dtypes("number").loc[:, df.select_dtypes("number").nunique() < 50]
    df_categorical = pd.concat([df.select_dtypes("object"), categorical_from_numerical], axis=1)
    df_numerical = df.select_dtypes("number").drop(columns=categorical_from_numerical.columns)
    return df_categorical, df_numerical
    
def group_west_east(df):
    west_germany_stations = [
    'Bremen Hbf', 'Lübeck Hbf', 'Heilbronn Hbf', 'Regensburg Hbf',
    'Aachen Hbf', 'Aschaffenburg Hbf', 'Augsburg Hbf', 'Bad Oldesloe',
    'Bamberg', 'Bielefeld Hbf', 'Bietigheim-Bissingen', 'Bochum Hbf',
    'Bonn Hbf', 'Braunschweig Hbf', 'Bruchsal', 'Darmstadt Hbf',
    'Singen(Hohentwiel)', 'Dortmund Hbf', 'Düsseldorf Flughafen',
    'Düsseldorf Hbf', 'Duisburg Hbf', 'Solingen Hbf', 'Stuttgart Hbf',
    'Essen Hbf', 'Frankfurt(Main)Hbf', 'Freiburg(Breisgau) Hbf',
    'Fürth(Bay)Hbf', 'Fulda', 'Gelsenkirchen Hbf', 'Gießen',
    'Göttingen', 'Trier Hbf', 'Tübingen Hbf', 'Hagen Hbf',
    'Hamburg-Harburg', 'Hamm(Westf)Hbf', 'Hanau Hbf', 'Hannover Hbf',
    'Heidelberg Hbf', 'Herford', 'Uelzen', 'Hildesheim Hbf', 'Ulm Hbf',
    'Ingolstadt Hbf', 'Kaiserslautern Hbf', 'Karlsruhe Hbf',
    'Kassel Hbf', 'Kiel Hbf', 'Koblenz Hbf', 'Köln Hbf',
    'Landshut(Bay)Hbf', 'Ludwigshafen(Rh)Hbf', 'Lüneburg', 'Mainz Hbf',
    'Mannheim Hbf', 'Wiesbaden Hbf', 'Mönchengladbach Hbf',
    'Worms Hbf', 'Würzburg Hbf', 'München Hbf', 'München Ost',
    'Münster(Westf)Hbf', 'Wuppertal Hbf', 'Neumünster', 'Neuss Hbf',
    'Neustadt(Weinstr)Hbf', 'Nürnberg Hbf', 'Oberhausen Hbf',
    'Offenburg', 'Oldenburg(Oldb)Hbf', 'Osnabrück Hbf',
    'Paderborn Hbf', 'Pforzheim Hbf', 'Plochingen', 'Rheine',
    'Rosenheim', 'Saarbrücken Hbf', 'Düsseldorf Flughafen Terminal',
    'Frankfurt(Main)Süd', 'Hamburg Dammtor', 'Hamburg Hbf',
    'Hamburg-Altona', 'Kassel-Wilhelmshöhe', 'Köln Messe/Deutz',
    'München-Pasing', 'Wolfsburg Hbf'
    ]
    
    east_germany_stations = [
    'Berlin-Lichtenberg', 'Cottbus Hbf', 'Dresden Hbf', 'Dresden-Neustadt',
    'Erfurt Hbf', 'Frankfurt(Oder)', 'Halle(Saale)Hbf', 'Chemnitz Hbf',
    'Leipzig Hbf', 'Magdeburg Hbf', 'Berlin Ostbahnhof', 'Rostock Hbf',
    'Berlin-Spandau', 'Berlin-Wannsee', 'Berlin Zoologischer Garten',
    'Berlin Gesundbrunnen', 'Berlin Südkreuz', 'Berlin Potsdamer Platz',
    'Berlin Hbf', 'Flughafen BER', 'Berlin Friedrichstraße',
    'Potsdam Hbf', 'Weimar', 'Berlin Ostkreuz'
    ]

    df.loc[df["station"].isin(west_germany_stations), "former"] = "West"
    df.loc[df["station"].isin(east_germany_stations), "former"] = "East"
    
    return df
            