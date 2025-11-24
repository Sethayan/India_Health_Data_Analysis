from flask import Flask, jsonify, render_template, request
from data import load_all_data
from overview_stats import get_national_stats, get_insights, get_overview_ranking, get_shortfall
from comparison import get_comparison_data, get_yearly_comparison
from state_view import get_state_stats
from district_view import get_district_data
import json

app = Flask(__name__)

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

@app.route('/state/<state_name>')
def state_view(state_name):
    state_stats = get_state_stats(state_name, dataframes)
    national_stats = get_national_stats(dataframes)
    
    comparison = {}
    if 'function_infra_rural' in dataframes and not dataframes['function_infra_rural'].empty:
        df = dataframes['function_infra_rural']
        state_data = df[df['State/UT'] == state_name]
        if not state_data.empty:
            row = state_data.iloc[0]
            comparison['infra'] = {
                'sc_2005': int(row['Sub Centre 2005']),
                'sc_2023': int(row['Sub Centre 2023']),
                'phc_2005': int(row['PHCs 2005']),
                'phc_2023': int(row['PHCs 2023']),
                'chc_2005': int(row['CHCs 2005']),
                'chc_2023': int(row['CHCs 2023']),
            }
    
    return render_template('state_view.html', 
                          state_stats=state_stats, 
                          national_stats=national_stats,
                          comparison=comparison,
                          state_name=state_name)

@app.route('/districts')
def districts():
    district_data = get_district_data(dataframes)
    return render_template('districts.html', 
                          states=district_data['states'],
                          districts=json.dumps(district_data['districts']))

@app.route('/comparison')
def comparison():
    comparison_data = get_comparison_data(dataframes)
    yearly_data = get_yearly_comparison(dataframes)
    
    return render_template('comparison.html', 
                          comparison_data=json.dumps(comparison_data),
                          yearly_data=json.dumps(yearly_data))

def get_state_list():
    if 'sc_phc_chc_count' in dataframes and not dataframes['sc_phc_chc_count'].empty:
        return dataframes['sc_phc_chc_count']['State/UT'].tolist()
    return []

@app.context_processor
def inject_common_data():
    return {
        'states': get_state_list()
    }

dataframes = load_all_data()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 