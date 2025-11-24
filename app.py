from flask import Flask, jsonify, render_template, request
from data import load_all_data
from overview_stats import get_national_stats, get_insights, get_overview_ranking, get_shortfall
from comparison import get_comparison_data, get_yearly_comparison
import json

app = Flask(__name__)

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


@app.route('/manpower')
def manpower():
    manpower_data = {}
    
    if 'mo_phc_rural' in dataframes and not dataframes['mo_phc_rural'].empty:
        df = dataframes['mo_phc_rural'].copy()
        manpower_data['doctors'] = df.to_dict('records')

    if 'specialist_chc_rural' in dataframes and not dataframes['specialist_chc_rural'].empty:
        df = dataframes['specialist_chc_rural'].copy()
        manpower_data['specialists'] = df.to_dict('records')
    
    if 'nursing_rural' in dataframes and not dataframes['nursing_rural'].empty:
        df = dataframes['nursing_rural'].copy()
        manpower_data['nursing'] = df.to_dict('records')

    if 'pharmacist_rural' in dataframes and not dataframes['pharmacist_rural'].empty:
        df = dataframes['pharmacist_rural'].copy()
        manpower_data['pharmacists'] = df.to_dict('records')
        
    return render_template('manpower.html', manpower_data=json.dumps(manpower_data))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)