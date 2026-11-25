import pandas as pd

def analyze_crime():

    data = pd.read_csv("crime_data.csv")

    result = []

    grouped = data.groupby("location")

    for location, group in grouped:

        crime_count = len(group)
        crime_types = ", ".join(group["crime_type"].unique())

        result.append({
            "location": location,
            "count": crime_count,
            "types": crime_types
        })

    return result