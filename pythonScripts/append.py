import sqlite3

connection = sqlite3.connect("./anthems.db")
cursor = connection.cursor()

England = ["England", "Jerusalem", "1916", "William Blake", "Hubert Parry", "https://en.wikipedia.org/wiki/Jerusalem_(song)", "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png", ""]
ni = ["northern Ireland", "Londonderry Air", "1910", "Traditional", "Traditional", "https://en.wikipedia.org/wiki/Londonderry_Air", "//upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Empty_flag.svg/40px-Empty_flag.svg.png", ""]
scotland = ["Scotland", "Flower of Scotland", "1974", "Roy Williamson", "Roy Williamson", "https://en.wikipedia.org/wiki/Flower_of_Scotland", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Flag_of_Scotland.svg/40px-Flag_of_Scotland.svg.png", ""]
wales = ["Wales", "Hen Wlad Fy Nhadau", "1856", "James James", "James James", "https://en.wikipedia.org/wiki/Hen_Wlad_Fy_Nhadau", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Flag_of_Wales.svg/40px-Flag_of_Wales.svg.png", ""]


England = ["England", "https://upload.wikimedia.org/wikipedia/commons/b/b6/HWW_And_Did_Those_Feet.ogg", "https://upload.wikimedia.org/wikipedia/en/thumb/b/be/Flag_of_England.svg/40px-Flag_of_England.svg.png", ""]
ni = ["northern Ireland", "https://upload.wikimedia.org/wikipedia/commons/3/31/Londonderry_Air.ogg", "//upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Empty_flag.svg/40px-Empty_flag.svg.png", ""]
scotland = ["Scotland","https://upload.wikimedia.org/wikipedia/en/f/f4/Flower_of_Scotland.mp3", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Flag_of_Scotland.svg/40px-Flag_of_Scotland.svg.png", ""]
wales = ["Wales",  "https://upload.wikimedia.org/wikipedia/commons/0/02/Hen_Wlad_fy_Nhadau_piano.ogg", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Flag_of_Wales.svg/40px-Flag_of_Wales.svg.png", ""]


countries = [England, ni, scotland, wales]
for country in countries:
    print(country[:])
    cursor.execute("""
    UPDATE anthems
    SET Audio = ?, flag_link = ?
    WHERE state = ?
""", (country[1], country[2], country[0]))
connection.commit()
connection.close()