# import necessary libraries
from flask import (
    Flask,
    render_template)
import pandas as pd
import key
API_KEY = key.API_KEY
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################

# create route that renders html templates
@app.route("/")
def home():
    ##############################################################
    # Pull data from SQL datadase and turn it into JSON and cache
    ##############################################################
    state_heatmap=pd.read_csv('state_heatmap.csv')
    state_heatmap=state_heatmap.to_json(orient='records')
    state_heatmap=state_heatmap.replace("'",r"\'")

    usa_heatmap=pd.read_csv('usa_heatmap.csv')
    usa_heatmap=usa_heatmap.to_json(orient='records')
    usa_heatmap=usa_heatmap.replace("'",r"\'")

    county_heatmap=pd.read_csv('county_heatmap.csv')
    county_heatmap=county_heatmap.to_json(orient='records')
    county_heatmap=county_heatmap.replace("'",r"\'")

    return render_template("index.html", state_heatmap=state_heatmap, usa_heatmap=usa_heatmap, county_heatmap=county_heatmap, API_KEY=API_KEY)

@app.route("/plots")
def plots():
    ##############################################################
    # Pull data from SQL datadase and turn it into JSON and cache
    ##############################################################

    # Check and see if it is chaches already

    orders=pd.read_csv('Orders.csv')
    orders=orders.to_json(orient='records')

    state_cases=pd.read_csv('state_cases.csv')
    state_cases=state_cases.to_json(orient='records')

    state_deaths=pd.read_csv('state_deaths.csv')
    state_deaths=state_deaths.to_json(orient='records')

    usa_heatmap=pd.read_csv('usa_heatmap.csv')
    usa_heatmap=usa_heatmap.to_json(orient='records')
    usa_heatmap=usa_heatmap.replace("'",r"\'")

    county_cases=pd.read_csv('county_cases.csv')
    county_cases=county_cases.to_json(orient='records')
    county_cases=county_cases.replace("'",r"\'")

    county_deaths=pd.read_csv('county_deaths.csv')
    county_deaths=county_deaths.to_json(orient='records')
    county_deaths=county_deaths.replace("'",r"\'")

    return render_template("plots.html", orders=orders, state_cases=state_cases, state_deaths=state_deaths, usa_heatmap=usa_heatmap, county_cases=county_cases, county_deaths=county_deaths)

@app.route("/methodology")
def methodology():
    return render_template("methodology.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=False)