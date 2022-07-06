# Project-3-Connectivity
Visualising Internet Usage Around the World

# Contributors
### -
### -
### -
### -

# Description:

We sourced data on Global internet usage and connectivity over the years. Which we then cleaned, stored in a  SQL database online so we could fetch it using our Flask-Powered API and visualise the different datasets in mutliple ways with dynamic and interactive Map and Charts with submit buttons and year sliders. 

#	Our Theme: 
### Visualising Global Internet and Phone Usage:

•	Individuals using the internet 
•	Fixed broadband subscription
•	Mobile Cellular subscription 
•	Secure Internet Servers
•	Fixed telephone subscriptions

# Types of visualisations:

- Ineractive Line Graph visualising World Regions connectivity data collected by the ITU from 2005 to 2021

- Interactive Bar chart visualising world countries connectivity data collected by the World Bank from 2000 to 2020 which connects with world map when option is submitted.

- Interactive World Map with dynamic legend that changes according to datasets with a year slider from 2000-2020. Same dataset as the countries chart is used here and the submit button in that chart also controls the map.

- Interactive Grouped Bar Chart for World Regions Gender and Age connectivity data collected by the ITU.

# Dashboard
### This Dashboard has business and developmental uses.
From our dashboard you can view the changes in internet and phone usage in countries and regions around the world. There is a clear increase in mobile phones as landlines decrease. In some parts of the world people's first, and often only, connection to the internet is through mobile phones. 



# Data Sources:
We used two large datasets from two different sources: World Bank and ITU, and Countries Location dataset from Kaggle.

### - World Bank
### - ITU
### - Kaggle




# Technologies:
### •	Database: 
pgAdmin/SQL-Postgres using Heroku

### •	Python Flask-powered API:
To automatically fetch data and render the template

### •	Python using Pandas Jupyter Notebook:
To clean the data for the data cleaning function we used to load our data

### •	HTML / CSS:
For the index.html layout and to render our charts

### •	JavaScript:
for plotting the interactive charts

# JS Libraries:
### •	Highcharts – Useful for complex chart types with fully fledged customisations:
https://www.highcharts.com/blog/download/

### •	Plotly.js - Open Source Graphing Libraries:
https://plotly.com/graphing-libraries/ 



# Steps taken with photos

### Step 1

Drawing out how we envision our dashboard to be
•	Sketch of our planned visualisations


### Step 2
Finding the relevant data.
•	Screenshot of datsets
•	Sketch of metadata


### Step 3
Extracting the relevant data, cleaning it and finaly merging with the location dataset 
•	Screenshot Jupyter Notebook

### Step 4
Putting all of Step 3's data extraction and transformation in a function so we can load the data to our database for our charts and map.
•	Screenshot of main.py

### Step 5

Using Flask-Powered API to connect to our database, fetch and laod data
•	Screenshot of app.py

### Step 6
Plotting the datasets saved under relevant variables in the output in main.py and app.py.
•	Screenshot of app.js

### Step 7
We pulled the data from app.py and accessed it in our template so we could plot in our charts and map. Using the CSS and HTML attributes to positon our charts in the dashboard.
•	Screenshot of index.html
•	Screenshot of style.css

### Final Dashboard
•	Screenshot of the final dashboard



# How to run this:
### - Locally:

### - Online:





