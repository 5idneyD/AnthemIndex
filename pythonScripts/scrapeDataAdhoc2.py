import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3


allAnthems = requests.get("https://en.wikipedia.org/wiki/List_of_national_anthems").text
soup = BeautifulSoup(allAnthems, "html.parser")
# Set the option to display all columns
# pd.set_option('display.max_columns', None)
table = soup.find("table", {"class": "wikitable plainrowheaders sortable"})

connection = sqlite3.connect("./anthems.db")
cursor = connection.cursor()
for row in table.find_all("tr")[1:]:
    try:
        country = row.find_all("th")[0].text.strip()  # Get the country name from the header cell
        span = row.find_all("span", {"typeof": "mw:File"})[-1].find_all("source")[0]["src"]
        # source = span.find_all("source")
        split_span = span.split("/")[-1]
        if split_span[-4:] == ".mp3":
            split_span = split_span[:-4]
        full_link = "https://en.wikipedia.org/wiki/File:" + split_span
        # # print(f"Updating anthem audio page for {country}: {full_link}")
        
        cursor.execute("UPDATE anthems SET anthem_audio_page = ? WHERE state = ?", (full_link, country))
    except:
        continue
# # Save the DataFrame to a SQLite database
# connection = sqlite3.connect("anthems.db")
# df.to_sql(name="anthems",  con=connection, if_exists="replace", index=True)
connection.commit()
connection.close()
