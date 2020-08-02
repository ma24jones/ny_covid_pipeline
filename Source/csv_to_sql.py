# into a PostgreSQL table

from sqlalchemy import create_engine

import psycopg2

import pandas as pd

data_path = "/Users/matthewjones/Dev/Data_Engineering_Projects/ny_covid_pipeline/Data/NY_COVID-19_Testing.csv"
ny_covid_df = pd.read_csv(data_path)

engine = create_engine("postgresql+psycopg2://localhost:5432/matthewjones")
postgreSQLConnection = engine.connect()
postgreSQLTable = "NYCovidData"


try:

    frame = ny_covid_df.to_sql(
        postgreSQLTable, postgreSQLConnection, if_exists="replace", index=False
    )

except ValueError as vx:

    print(vx)

except Exception as ex:

    print(ex)

else:

    print("PostgreSQL Table %s has been created successfully." % postgreSQLTable)

finally:

    postgreSQLConnection.close()

