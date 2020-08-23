# NY State COVID-19 Pipeline

A data pipeline that:
- Connects to the [NY Statewide COVID-19 Testing](https://health.data.ny.gov/browse?tags=covid-19) API.
- Stores data in a Postgres database.
- Produces a line chart displaying Albany County "new positive" cases over time.
- Gives a 5 day summarized view of COVID-19 results for Albany County.
- Sends an automated email that includes the line graph and summary exhibit.

## Technologies
Project is created with:
- Python 3.8.5
- pandas 1.1.0
- matplotlib 3.3.1
- apache-airflow 1.10.11
- Postgres 2.3.5

## Line Graph Output
![Albany County COVID-19 Line Graph](./Visualization/line%20plot.jpg)
