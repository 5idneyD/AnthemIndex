from flask import Flask, send_from_directory, Response, jsonify
import os
import mimetypes
from flask_cors import CORS
import sqlite3

app = Flask(__name__, static_folder="dist", static_url_path="")
CORS(app)
# Make sure .js files are served as application/javascript
mimetypes.add_type("application/javascript", ".js")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/hello")
def hello():
    return jsonify(message="Hello from Flask!")

@app.route("/<country>")
def country(country):
    return send_from_directory(app.static_folder, "index.html")

# Catch-all route for Vue's client-side routing
@app.route("/api/<country>")
def static_proxy(country):
    connection = sqlite3.connect("anthems.db")
    cursor = connection.cursor()
    for data in cursor.execute("SELECT * FROM anthems WHERE state = ?", (country,)):
        print(data)
        anthem_data = {
            "country": data[1],
            "anthem_name": data[2],
            "composer": data[5],
            "lyricist": data[4],
            "year": data[3],
            "source": data[6],
            "flag_link": data[7],
            "lyrics": data[8]
        }
    connection.close()
    return jsonify(anthem_data)





if __name__ == "__main__":
    app.run(debug=True)