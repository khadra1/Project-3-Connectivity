# Project-3-Connectivity
Visualising Internet Usage Around the World

# Contributors
### - Khadra
### - Chisimnulia
### - Kudzanai 


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
From our dashboard you can view the changes in internet and phone usage in countries and regions around the world. There is a clear increase in mobile phones as landlines decrease. In some parts of the world people's first, and often only, connection to the internet is through mobile phones. 



# Data Sources:
We used two large datasets from two different sources: World Bank and ITU, and Countries Location dataset from Kaggle.

### - Connectivity Data from the World Bank: 
https://data.worldbank.org/indicator/IT.NET.USER.ZS

### - Connectivity Data from the ITU (UN Agency for IT and Communication): 
https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx

### - Countries Location Data from Kaggle: 
https://www.kaggle.com/datasets/qramkrishna/world-coordinates?select=world_country.csv




# Technologies:
### •	Database: 
MongoDB using Flask-PyMongo 

### •	Python Flask-powered API:
To automatically fetch data and render the template

### •	Python using Pandas Jupyter Notebook:
To clean the data for the data cleaning function we used to load our data

### •	HTML / CSS:
For the index.html layout and to render our charts

### •	JavaScript:
For plotting the interactive charts

# JS Libraries:
### •	Highcharts – Useful for complex chart types with fully fledged customisations:
https://www.highcharts.com/blog/download/

### •	Plotly.js - Open Source Graphing Libraries:
https://plotly.com/graphing-libraries/ 



# Steps taken 
### Step 1

Drawing out how we envision our dashboard to be
•	Sketch of our planned visualisations
![image](https://user-images.githubusercontent.com/67019030/177653668-49bde6f8-7cb4-43da-b0ee-0020d264505d.jpeg)


### Step 2
Finding the relevant data.

### Step 3
Extracting the relevant data, cleaning it and finaly merging with the location dataset 
•	See Jupyter Notebook

### Step 4
Putting all of Step 3's data extraction and transformation in a function so we can load the data to our database for our charts and map.
•	See main.py

### Step 5

Using Flask-Powered API to connect to our database, fetch the cleaned data from main.py and load data onto our MongoDB database.
•	See app.py

### Step 6
Plotting the datasets saved under relevant variables in the output in main.py and app.py.
•	See app.js

### Step 7
We pulled the data from app.py and accessed it in our template so we could plot in our charts and map. Using the CSS and HTML attributes to positon our charts in the dashboard.
•	See index.html
•	See style.css

### Final Dashboard

•	Screenshot of the final dashboard

![dashboard](https://user-images.githubusercontent.com/67019030/177653123-feb85636-1ee5-4746-a658-58879d3c91a8.png)



# How to run this:
### Locally:
Clone the GitHub repository and create a virtual environment using the follwing commands for your Operating System:

### On Linux:
1. If pip is not in your system:
`$ sudo apt-get install python-pip`

2. Then install virtualenv
`$ pip install virtualenv`

3. Now check your installation
`$ virtualenv --version`

4. Create a virtual environment now
`$ virtualenv virtualenv_name`

5. Finally activate the virtual environment inside the directory for this project:
`$ source virtualenv_name/bin/activate`

### On Windows:
1. If pip isn't present you can install it using pip
`python get-pip.py`

2. Then install virtualenv
`pip install virtualenv`

3. Create a virtual environment now
`virtualenv --python C:\Path\To\Python\python.exe venv`

4. Finally actiivate teh virtual environment inside the directory for this project:
`.\venv\Scripts\activate`

### On Mac
1. If pip isn't present you can install it using pip
`sudo easy_install pip`

2. Then install virtualenv
`sudo pip install virtualenv``

3. Create a virtual environment now
`virtualenv env`

4. Finally actiivate teh virtual environment inside the directory for this project:
`source env/bin/activate`



Finally download the relevenant dependencies by using the command pip `freeze > requirements.txt`

You can now run this project locally!

