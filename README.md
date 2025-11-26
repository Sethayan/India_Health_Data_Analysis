##  Project Description

Motivation

Government departments hold vast amounts of key data across areas such as healthcare, infrastructure, and economics. However, much of this data is stored in formats that are difficult for the public to consume and not ideal for policy makers. With initiatives like Digital India, the volume of digitized data is growing rapidly, but accessibility and usability remains a challenge.

Problem Statement
This project aims to address these issues by focusing on the visualization of healthcare data. We have built a web application to present this data in a clear and interactive manner. The goal is to make raw datasets easier to interpret, enabling both citizens and policymakers to derive meaningful insights quickly.




## Team Name
Bit by bit

##  Team Members

1. Mohit Thorat (25m0765)
2. Ayan seth( 25m0804)
3. Kamal Charotia (25m0814)

## Project Structure

Healthcare Dashboard Project (Code)
├── .env
├── .gitignore
├── app.py
├── appDatabase.db
├── askai.py
├── comparison.py
├── data/
├── data (Obsolete).py
├── database.py
├── district_view.py
├── health_indicator.py
├── manpower.py
├── overview_stats.py
├── requirements.txt
├── state_view.py
├── static/
│   ├── css/
│   │   └── style.css
│   ├── geoJSON/
│   │   └── india.geoJSON
│   └── js/
│       ├── askai.js
│       ├── comparison_view.js
│       ├── district.js
│       ├── health_indicator.js
│       ├── manpower.js
│       ├── overview_charts.js
│       ├── state_view.js
│       └── utility.js
├── templates/
│   ├── ask_ai.html
│   ├── comparison.html
│   ├── dashboard.html
│   ├── districts.html
│   ├── health_indicators.html
│   ├── layouts/
│   │   └── base.html
│   ├── manpower.html
│   ├── navbar.html
│   └── state_view.html


## Role of each file

# app.py
Entry point of the flask application containing routes

# appDatabase.db
SqlLite database file

# askai.py
Backend logic for the Ask AI module

# comparison.py
Backend logic for the Comparison module

# data (Obsolete).py
Contains mapping of the table name with their extracted csv file

# database.py
Contains model definition for SqlAlchemy python module

# district_view.py
Backend logic for the District View module

# health_indicator.py
Backend logic for the Health Care Indicator module

# manpower.py
Backend logic for the Manpower module

# overview_stats.py
Backend logic for the Overview Stat module

# state_view.py
Backend logic for the State View module

# css/style.css
Application style sheet

# geoJSON/india.geoJSON
Map file of India for heatmap in overview stat module

# js/askai.js
Front end logic of Ask AI Module

# comparison_view.js
Front end logic for the Comparison module

# district.js
Front end logic for the District View module

# health_indicator.js
Front end logic for the Health Care Indicator module

# manpower.js
Front end logic for the Manpower module

# overview_charts.js
Front end logic for the Overview Stat module

# state_view.js
Front end logic for the State View module

# ask_ai.html
Ask AI module html template

# comparison.html
Comparison module html template

# dashboard.html
Overview stat module html template

# districts.html
District View module html template

# health_indicators.html
Health Indicator module html template

# manpower.html
Manpower module html template

# navbar.html
Navigation Bar html template

# state_view.html
State View module html template

# base.html
Base layout of application