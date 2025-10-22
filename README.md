# India Health Data Analysis Dashboard

A Flask-based web application that visualizes key  Health Indicators of India such as Life Expectancy at Birth , Infant Mortality Rate , and Maternal Mortality Ratio using interactive charts and data visualizations.

---

##  Project Description

The **India Health Data Analysis Dashboard** is designed to help users, researchers, and policymakers explore the current state of health across Indian states.  
It provides visual insights into critical public health indicators that reflect overall healthcare quality and population well-being.

Users can:
- Select a state to view its health statistics.
- Analyze trends through dynamic and interactive charts.
- Understand how states compare in terms of mortality and life expectancy.

The application is built using **Flask** for the backend and **Chart.js** for interactive front-end data visualization.

---

##  Team Members

1. Mohit Thorat 25M0765 
2. Ayan seth  25M0804
3. Kamal Charotia 25M0814

---

##  Features

-  **Life Expectancy at Birth:**  
  Average number of years a newborn is expected to live under current mortality conditions.

-  **Infant Mortality Rate (IMR):**  
  Number of infant deaths per 1,000 live births.

-  **Maternal Mortality Ratio (MMR):**  
  Number of maternal deaths per 100,000 live births.

-  **State-wise Health Infrastructure Visualization:**  
  Interactive bar charts powered by Chart.js.

-  **Physicians per 1000 people bar chart:**  
  Clean and easy-to-use interface designed for clarity and accessibility.

---

##  Installation Procedure

Follow these steps to set up and run the project locally:

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Create and Turn on virtual environment.
3. Install the required packages inside virtual environment:
   ```bash
   pip install -r requirements.txt
4. Run flask app
   ```bash
   flask run --debug
6. Go to the 127.0.0.1:5000 port to access the working site. 
7. Visit urls 
a)127.0.0.1:5000\state <br>
b)127.0.0.1:5000\country <br>
c)127.0.0.1:5000\state\\{statename} <br>