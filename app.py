from flask import Flask, jsonify, render_template, request
from overview_stats import get_national_stats, get_insights, get_overview_ranking, get_shortfall
from comparison import get_comparison_data, get_yearly_comparison
from state_view import get_state_stats, get_state_comparison_data, get_state_list_data
from district_view import get_district_data
from health_indicator import get_health_indicator
from manpower import get_manpower_data
from askai import processQuery
import json

app = Flask(__name__)


@app.route('/')
def dashboard():
    national_stats = get_national_stats()
    insights = get_insights()
    rankings = get_overview_ranking()
    shortfall_data = get_shortfall()

    return render_template('dashboard.html',
                           national_stats=national_stats,
                           insights=insights,
                           rankings=rankings,
                           shortfall_data=json.dumps(shortfall_data))

@app.route('/health-indicators')
def health_indicators():
    indicators = get_health_indicator()
    return render_template('health_indicators.html',
                           indicators=json.dumps(indicators))


@app.route('/manpower')
def manpower():
    manpower_data = get_manpower_data()
    return render_template('manpower.html', manpower_data=json.dumps(manpower_data))


@app.route('/state/<state_name>')
def state_view(state_name):
    state_stats = get_state_stats(state_name)
    national_stats = get_national_stats()

    comparison = get_state_comparison_data(state_name)

    return render_template('state_view.html',
                           state_stats=state_stats,
                           national_stats=national_stats,
                           comparison=comparison,
                           state_name=state_name)


@app.route('/districts')
def districts():
    district_data = get_district_data()
    return render_template('districts.html',
                           states=district_data['states'],
                           districts=json.dumps(district_data['districts']))


@app.route('/comparison')
def comparison():
    comparison_data = get_comparison_data()
    yearly_data = get_yearly_comparison()

    return render_template('comparison.html',
                           comparison_data=json.dumps(comparison_data),
                           yearly_data=json.dumps(yearly_data))

@app.route('/ask-ai')
def ask_ai():
    return render_template('ask_ai.html')

@app.route('/api/ask-ai', methods=['POST'])
def api_ask_ai():
    data = request.get_json()
    query = data.get('query', '')
    if not query:
        return jsonify({'answer': 'Please provide a query to answer', 'success': False}), 400
        
    result = processQuery(query)
    return jsonify(result)

def get_state_list():
    return get_state_list_data()

@app.context_processor
def inject_common_data():
    return {
        'states': get_state_list()
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)