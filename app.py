from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from scripts.main import load_data


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/connectivity_app")
db = mongo.db
    
@app.route("/", methods =["GET", "POST"])
def plot_chart():

    if request.method == "POST":
        filter1 = request.form.get("filter1")
        filter2 = request.form.get("filter2")
        data = load_data(filter1,filter2)
        return render_template("index.html", data=data)
    data = load_data('Fixed broadband subscriptions','Zimbabwe')
    # Save the cleaned data to the database
    conn_db = mongo.db.connectivity
    conn_db.drop()
    conn_db.update_one({}, {"$set": data}, upsert=True)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)