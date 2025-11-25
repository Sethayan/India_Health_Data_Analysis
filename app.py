from flask import Flask, jsonify, render_template, request
from data import load_all_data
from overview_stats import get_national_stats, get_insights, get_overview_ranking, get_shortfall
import json
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from models import MoPhcRural, SpecialistChcRural, NursingRural, PharmacistRural
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Configure SQLite database
# This creates a file named 'health_data.db' in your project folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'health_data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
def row_to_dict(row):
    """
    Converts a SQLAlchemy Model object to a dictionary.
    
    CRITICAL: This maps the 'Python Attribute' value back to the 'DB Column Name' key.
    Example: 
      Model has: required = db.Column('Required 2023', ...)
      Result dict: {'Required 2023': 500}
      
    This ensures your frontend (which looks for 'Required 2023') continues to work.
    """
    data = {}
    for column in row.__table__.columns:
        # column.name is the Database name (e.g., "Required 2023")
        # column.key is the Python attribute name (e.g., "required")
        data[column.name] = getattr(row, column.key)
    return data

def fetch_data(model_class):
    """Safely queries the DB and returns a list of dicts."""
    try:
        results = db.session.query(model_class).all()
        return [row_to_dict(row) for row in results]
    except Exception as e:
        print(f"❌ Error querying {model_class.__tablename__}: {e}")
        return []
# Routes
@app.route('/')
def dashboard():
    national_stats = get_national_stats(dataframes)
    insights = get_insights(dataframes)
    rankings = get_overview_ranking(dataframes)
    shortfall_data = get_shortfall(dataframes)

    return render_template('dashboard.html', 
                          national_stats=national_stats, 
                          insights=insights,
                          rankings=rankings,
                          shortfall_data=json.dumps(shortfall_data))

@app.route('/api/national-stats')
def api_national_stats():
    return jsonify(get_national_stats(dataframes))

dataframes = load_all_data()


@app.route('/health-indicators')
def health_indicators():
    indicators = {}
    
    if 'imr' in dataframes and not dataframes['imr'].empty:
        indicators['imr'] = dataframes['imr'].to_dict('records')
    
    if 'birth_death_rate' in dataframes and not dataframes['birth_death_rate'].empty:
        indicators['birth_death'] = dataframes['birth_death_rate'].to_dict('records')

    if 'state_density' in dataframes and not dataframes['state_density'].empty:
        indicators['density'] = dataframes['state_density'].to_dict('records')

    return render_template('health_indicators.html',
                          indicators=json.dumps(indicators))


# @app.route('/manpower')
# def manpower():
#     manpower_data = {}
    
#     if 'mo_phc_rural' in dataframes and not dataframes['mo_phc_rural'].empty:
#         df = dataframes['mo_phc_rural'].copy()
#         manpower_data['doctors'] = df.to_dict('records')

#     if 'specialist_chc_rural' in dataframes and not dataframes['specialist_chc_rural'].empty:
#         df = dataframes['specialist_chc_rural'].copy()
#         manpower_data['specialists'] = df.to_dict('records')
    
#     if 'nursing_rural' in dataframes and not dataframes['nursing_rural'].empty:
#         df = dataframes['nursing_rural'].copy()
#         manpower_data['nursing'] = df.to_dict('records')

#     if 'pharmacist_rural' in dataframes and not dataframes['pharmacist_rural'].empty:
#         df = dataframes['pharmacist_rural'].copy()
#         manpower_data['pharmacists'] = df.to_dict('records')
        
#     return render_template('manpower.html', manpower_data=json.dumps(manpower_data))
# @app.route('/manpower')
# def manpower():
#     manpower_data = {}
    
#     print("--- DEBUG: Fetching Manpower Data ---")

#     # 1. Doctors
#     doctors_list = db.session.query(MoPhcRural).all()
#     manpower_data['doctors'] = [row_to_dict(row) for row in doctors_list]
#     print(f"Doctors found: {len(manpower_data['doctors'])}")

#     # 2. Specialists
#     specialists_list = db.session.query(SpecialistChcRural).all()
#     manpower_data['specialists'] = [row_to_dict(row) for row in specialists_list]
#     print(f"Specialists found: {len(manpower_data['specialists'])}")

#     # 3. Nursing
#     nursing_list = db.session.query(NursingRural).all()
#     manpower_data['nursing'] = [row_to_dict(row) for row in nursing_list]

#     # 4. Pharmacists
#     pharmacists_list = db.session.query(PharmacistRural).all()
#     manpower_data['pharmacists'] = [row_to_dict(row) for row in pharmacists_list]
        
#     # Print the FINAL data structure to check
#     #print(json.dumps(manpower_data)) 

# @app.route('/manpower')
# def manpower():
#     manpower_data = {}
    
#     print("--- DEBUG: Fetching Manpower Data (ORM getattr) ---")

#     # 1. Doctors
#     manpower_data['doctors'] = fetch_table_data(MoPhcRural)
#     print(f"Doctors found: {len(manpower_data['doctors'])}")

#     # 2. Specialists
#     manpower_data['specialists'] = fetch_table_data(SpecialistChcRural)
    
#     # 3. Nursing
#     manpower_data['nursing'] = fetch_table_data(NursingRural)

#     # 4. Pharmacists
#     manpower_data['pharmacists'] = fetch_table_data(PharmacistRural)
        
#     return render_template('manpower.html', manpower_data=json.dumps(manpower_data))
@app.route('/manpower')
def manpower():
    manpower_data = {}
    
    print("\n--- DEBUG: Fetching Manpower Data (Explicit Models) ---")

    # 1. Doctors
    manpower_data['doctors'] = fetch_data(MoPhcRural)
    print(f"Doctors found: {len(manpower_data['doctors'])}")

    # 2. Specialists
    manpower_data['specialists'] = fetch_data(SpecialistChcRural)
    
    # 3. Nursing
    manpower_data['nursing'] = fetch_data(NursingRural)

    # 4. Pharmacists
    manpower_data['pharmacists'] = fetch_data(PharmacistRural)
        
    return render_template('manpower.html', manpower_data=json.dumps(manpower_data))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)