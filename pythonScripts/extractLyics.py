import sqlite3
import pandas as pd
import requests
from bs4 import BeautifulSoup

connection = sqlite3.connect("anthems.db")
countries = pd.read_sql_query("SELECT state FROM anthems", connection)
cursor = connection.cursor()
cursor.execute("ALTER TABLE anthems ADD COLUMN lyrics TEXT")  # Add a new column for lyrics if it doesn't exist
df = pd.DataFrame(columns=["country", "lyrics"])

for i in countries['State']:
    print(i)
    page = requests.get("https://www.nationalanthems.online/" + i.lower()).text
    soup = BeautifulSoup(page, "html.parser")
    lyrics = soup.find("div", {"class": "py-28 text-lg md:text:xl lg:text-2xl"})
    # df.loc[len(df)] = [i, lyrics.text.strip() if lyrics else "Lyrics not found"]

    cursor.execute("UPDATE anthems SET lyrics = ? WHERE state = ?", (lyrics.text.strip() if lyrics else "Lyrics not found", i))

connection.commit()
connection.close()