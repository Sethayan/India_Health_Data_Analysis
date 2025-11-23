from flask import Flask, render_template, request
from data import load_all_data

app = Flask(__name__)

# Routes
@app.route('/')
def dashboard():
    national_stats = get_national_stats(dataframes)
    
    return render_template('dashboard.html', 
                          national_stats=national_stats, 
                          insights=insights,
                          rankings=rankings,
                          shortfall_data=json.dumps(shortfall_data))

dataframes = load_all_data()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
