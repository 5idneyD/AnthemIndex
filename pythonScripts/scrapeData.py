import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

allAnthems = requests.get("https://en.wikipedia.org/wiki/List_of_national_anthems").text
soup = BeautifulSoup(allAnthems, "html.parser")
# Set the option to display all columns
# pd.set_option('display.max_columns', None)
table = soup.find("table", {"class": "wikitable plainrowheaders sortable"})
# print(table)


df = pd.DataFrame(columns=[cell.text.strip().replace("[a]", "") for cell in table.find_all("th")[:6]] + ["flag_link"])  # Add a column for the flag link
print(df.columns)
    
rows = table.find_all("tr")[1:]  # Skip the header row
for row in rows:
    try:
        data = []
        country = row.find_all("th")[0].text.strip()  # Get the country name from the header cell
        cells = row.find_all("td")
        anthem_name = cells[0].text.strip().replace("[b]", "")
        flag_link = row.find("img", {"class": "mw-file-element"})["src"]

        data.append(country)
        if len(cells) == 9:
            for cell in cells[:4]:
                data.append(cell.text.strip().replace("[b]", ""))
        else:
            for cell in cells[:3]:
                data.append(cell.text.strip().replace("[b]", ""))
            data.append(cells[2].text.strip())
        try:
            musicSourceCell = cells[4]
            source = "https:" + musicSourceCell.find_all("source")[0]["src"]
        except:
            musicSourceCell = cells[5]
            source = "https:" + musicSourceCell.find_all("source")[0]["src"]
        data.append(source)
        data.append("https:" + flag_link)  # Add the flag link to the data
        print(data)
        try:
            df.loc[len(df)] = data
        except ValueError:
            continue
    except IndexError:
        continue

# Save the DataFrame to a SQLite database
connection = sqlite3.connect("anthems.db")
df.to_sql(name="anthems",  con=connection, if_exists="replace", index=True)
connection.close()
