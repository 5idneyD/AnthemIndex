import os
import sqlite3

connection = sqlite3.connect("./anthems.db")
c = connection.cursor()

allAnthems = c.execute("select vocal_media from anthems").fetchall()

used = []
for i in allAnthems:
    used.append(i[0])

b = []
allVocalFiles = os.walk("./public/vocals/")
for i in allVocalFiles:
    b.append(i)
allVocalFiles = b[0][2]

for file in allVocalFiles:
    if file not in used:
        os.remove("C:\Dev\WebDev\AnthemIndex\\public\\vocals"+file)
