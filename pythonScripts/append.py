import sqlite3

connection = sqlite3.connect("./anthems.db")
cursor = connection.cursor()

England = ["England", "Jerusalem", "1916", "William Blake", "Hubert Parry", "https://en.wikipedia.org/wiki/Jerusalem_(song)", "https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_England.svg/1200px-Flag_of_England.svg.png", ""]
ni = ["northern Ireland", "Londonderry Air", "1910", "Traditional", "Traditional", "https://en.wikipedia.org/wiki/Londonderry_Air", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Ulster_banner.svg/1200px-Ulster_banner.svg.png", ""]
scotland = ["Scotland", "Flower of Scotland", "1974", "Roy Williamson", "Roy Williamson", "https://en.wikipedia.org/wiki/Flower_of_Scotland", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Flag_of_Scotland.svg/1200px-Flag_of_Scotland.svg.png", ""]
wales = ["Wales", "Hen Wlad Fy Nhadau", "1856", "James James", "James James", "https://en.wikipedia.org/wiki/Hen_Wlad_Fy_Nhadau", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Flag_of_Wales_2.svg/1200px-Flag_of_Wales_2.svg.png", ""]

countries = [England, ni, scotland, wales]
for country in countries:
    cursor.execute("""
    INSERT INTO anthems
    (state, "National anthem", "Date adopted (de jure)", lyricist, "composer/Artist", Audio, flag_link, lyrics)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", country)
connection.commit()
connection.close()