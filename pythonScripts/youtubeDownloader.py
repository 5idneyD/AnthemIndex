import yt_dlp
import sqlite3


url = {"state": "Canada", "link": "https://music.youtube.com/watch?v=JpFDNzrWK7Q"}

ydl_opts = {
    "format": "bestaudio/best",
    "download_ranges": lambda info, ydl: [{"start_time": 0, "end_time": 266}],  # accept 2 args
    "outtmpl": "C:/Dev/WebDev/AnthemIndex/public/vocals/%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url["link"], download=True)
    file_path = ydl.prepare_filename(info_dict)  # 👈 this gives you the expanded filename
    final_file_name = file_path.split("\\")[-1].replace(".webm", ".mp3")
    
connection = sqlite3.connect(r"C:\Dev\WebDev\AnthemIndex\anthems.db")
c = connection.cursor()
c.execute("UPDATE anthems set vocal_media=? where state=?", (final_file_name, url['state']))
connection.commit()
connection.close()

