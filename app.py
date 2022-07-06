# Import dpendencies for the Flask powered API
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
# import psycopg2
# Import the load_data function from main.py
import os
from scripts.main import load_data
# Create an instance of Flask
app = Flask(__name__)
# Using Heroku to connect to pgAdmin database and make it available online
db_url = os.environ.get("SQL_DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db = SQLAlchemy(app)
def create_database():
    db= create_engine(db_url)
    conn= db.connect()
    df = load_data()
    # Saving the cleaned_data from the laod function to SQL
    df.to_sql('data', con=conn, if_exists='replace',index=False)
    # conn = psycopg2.connect()
    #
@app.route("/", methods =["GET", "POST"])
def plot_chart():
    # create_database()
    # for loop for the option submitted and for loading it
    if request.method == "POST":
        filter1 = request.form.get("filter1")
        filter2 = request.form.get("filter2")
         # Call the load_data function which will load the cleaned data when users submit their option
        data = load_data(filter1,filter2)
        # Return template and data when option is submitted/changed
        return render_template("index.html", data=data)
        # Call the load_data function which will load the cleaned data when the page reloads
    data = load_data('Fixed broadband subscriptions','Zimbabwe')
         # Return template and data when page refreshes/is loaded
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()