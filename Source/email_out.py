import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import pandas as pd
import numpy as np
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
                        SELECT test_date as "Test Date", new_positives as "New Positives", total_number_of_tests as "Total Tests"
                        FROM 
                            "NYCovidData"
                        WHERE 
                            "county"='Albany'
                        """,
    con=conn,
    parse_dates="Test Date",
    index_col="Test Date",
)

sender_email = os.environ.get("EMAIL_1")
receiver_email = os.environ.get("EMAIL_2")
password = os.environ.get("APP_PASSWORD")

message = MIMEMultipart("related")
message["Subject"] = "Albany County COVID Update"
message["From"] = sender_email
message["To"] = receiver_email
message.preamble = "This is a multi-part message in MIME format."

df["% Positive"] = df["New Positives"] / df["Total Tests"]
table = df.tail()

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart("alternative")
message.attach(msgAlternative)

msgText = MIMEText("This is the alternative plain text message.")
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText(
    '<b>Hi!</b><br>Here is your daily COVID update.<br><img src="cid:image1"><br>{0}'.format(
        table.to_html(formatters={"% Positive": "{:,.2%}".format})
    ),
    "html",
)
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open(
    "/Users/matthewjones/Dev/Data_Engineering_Projects/ny_covid_pipeline/Visualization/line plot.jpg",
    "rb",
)
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header("Content-ID", "<image1>")
message.attach(msgImage)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Sent")

