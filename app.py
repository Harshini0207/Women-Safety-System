from flask import Flask, render_template
from analysis import analyze_crime
from map_generator import generate_map

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    crime_data = analyze_crime()
    return render_template("analysis.html", crimes=crime_data)

@app.route("/map")
def map_view():
    generate_map()
    return render_template("map.html")

@app.route("/alert")
def alert():
    return render_template("alert.html")

if __name__ == "__main__":
    app.run(debug=True)