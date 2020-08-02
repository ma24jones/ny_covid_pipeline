import pandas as pd
import os

# Reading JSON from NY Gov Covid API and saving as .csv file.
def jsonToCsv(url, outputcsv):
    data = pd.read_json(url)
    data.to_csv(outputcsv, index=False)

    return "Succesfully read JSON and written to .csv"


APP_TOKEN = os.environ.get("NY_COVID_APP_TOKEN")

json_url = f"https://health.data.ny.gov/resource/xdss-u53e.json?$$app_token={APP_TOKEN}"

jsonToCsv(
    json_url,
    "/Users/matthewjones/Dev/Data_Engineering_Projects/ny_covid_pipeline/Data/NY_COVID-19_Testing.csv",
)

