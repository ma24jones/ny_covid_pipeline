import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import os

user = os.environ.get("USER")

# Declaring the points for first line plot
conn = psycopg2.connect(
    database="matthewjones", user=user, host="localhost", port="5432"
)

df = pd.read_sql_query(
    """
                        SELECT *
                        FROM 
                            "NYCovidData"
                        WHERE 
                            "county"='Albany'
                        """,
    con=conn,
    parse_dates="test_date",
    index_col="test_date",
)

df.reset_index()
print(df.head())
# Setting the figure size
fig = plt.figure(figsize=(10, 5))
# plotting the first plot
plt.plot(df["new_positives"])
# Declaring the points for second line plot
# X2 = [1,2,3,4,5]
# Y2 = [1,4,9,16,25]
# plotting the second plot
# plt.plot(X2, Y2, label = "plot 2")

# Labeling the X-axis
plt.xlabel("Date")
# Labeling the Y-axis
plt.ylabel("New Positives")
# Give a title to the graph
plt.title("Albany County COVID-19 Update")

# Show a legend on the plot
# plt.legend()
# Saving the plot as an image
fig.savefig(
    "/Users/matthewjones/Dev/Data_Engineering_Projects/ny_covid_pipeline/Visualization/line plot.jpg"
)
# Showing the plot
