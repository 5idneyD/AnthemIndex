import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

allAnthems = requests.get("https://en.wikipedia.org/wiki/List_of_British_anthems").text
soup = BeautifulSoup(allAnthems, "html.parser")
# Set the option to display all columns
# pd.set_option('display.max_columns', None)
table = soup.find("table", {"class": "wikitable"})


df = pd.DataFrame(columns=[cell.text.strip().replace("[a]", "") for cell in table.find_all("th")[:6]] + ["flag_link"])  # Add a column for the flag link
print(df.columns)
    
rows = table.find_all("tr")[1:] 
# Skip the header row
for row in rows[:20]:
    print(row)# 
    try:
        data = []
        country = row.find_all("th")[0].text.strip()  # Get the country name from the header cell
        flag_link = row.find("img", {"class": "mw-file-element"})["src"]
        song = row.find_all("td")[0].text.strip().replace("[b]", "")
        lyricist = row.find_all("td")[2].text.strip().replace("[b]", "")
        composer = row.find_all("td")[3].text.strip().replace("[b]", "")
        year = row.find_all("td")[1].text.strip().replace("[b]", "")
        source = row.find_all("td")[4].text.strip().replace("[b]", "")
        data.append(country)
        data.append(song)
        data.append(lyricist)
        data.append(composer)
        data.append(year)
        data.append(source)
        data.append("https:" + flag_link)  # Add the flag link to the data
        try:
            df.loc[len(df)] = data
        except ValueError:
            continue
    except:
        data = []
        country = row.find_all("th")[0].text.strip()  # Get the country name from the header cell
        flag_link = row.find("img", {"class": "mw-file-element"})["src"]
        song = row.find_all("td")[0].text.strip().replace("[b]", "")
        lyricist = row.find_all("td")[2].text.strip().replace("[b]", "")
        composer = row.find_all("td")[2].text.strip().replace("[b]", "")
        year = row.find_all("td")[1].text.strip().replace("[b]", "")
        source = row.find_all("td")[3].text.strip().replace("[b]", "")
        data.append(country)
        data.append(song)
        data.append(lyricist)
        data.append(composer)
        data.append(year)
        data.append(source)
        data.append("https:" + flag_link)
print(df)
# # Save the DataFrame to a SQLite database
# connection = sqlite3.connect("anthems.db")
# df.to_sql(name="anthems",  con=connection, if_exists="replace", index=True)
# connection.close()
