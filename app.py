from flask import Flask, render_template, request
from data import load_all_data
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)