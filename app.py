from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# REST endpoint API to use
url = "https://testtechnext1-pearl118.b4a.run/search/api/query/?query="

# Main route for searching API using keyword provided
@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        keyword = request.form["keyword"]
        data = requests.get(url + keyword).json()
        count = 0
        for item in data:
            item["text"] = item["text"][2:-3]
            count += 1
        return render_template("index.html", keyword=keyword, data=data, count=count)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
