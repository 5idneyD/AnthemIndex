from flask import Flask, send_from_directory, Response, jsonify
import os
import mimetypes
# from flask_cors import CORS
import sqlite3
ROOT = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_folder="dist", static_url_path="")
# CORS(app)
# Make sure .js files are served as application/javascript
mimetypes.add_type("application/javascript", ".js")

@app.route("/")
@app.route("/null")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/hello")
def hello():
    return jsonify(message="Hello from Flask!")

@app.route("/<country>")
def country(country):
    return send_from_directory(app.static_folder, "country.html")

# Catch-all route for Vue's client-side routing
@app.route("/api/<country>")
def static_proxy(country):
    connection = sqlite3.connect(os.path.join(ROOT, "anthems.db"))
    anthem_data = {}
    cursor = connection.cursor()
    for data in cursor.execute("SELECT * FROM anthems WHERE state = ?", (country,)):
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

@app.route("/api/countries")
def get_countries():
    connection = sqlite3.connect(os.path.join(ROOT, "anthems.db"))
    cursor = connection.cursor()

    # Fetch just the country column
    cursor.execute("SELECT state, flag_link FROM anthems")
    rows = cursor.fetchall()

    # Flatten list of tuples into a list of strings
    all_anthem_data = [[row[0], row[1]] for row in rows]
    all_anthem_data.append("All Countries")  # Add "All Countries" option

    connection.close()
    return jsonify(all_anthem_data)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)