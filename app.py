from flask import Flask, jsonify, render_template, request
from data import load_all_data
from overview_stats import get_national_stats, get_insights, get_overview_ranking, get_shortfall
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
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
