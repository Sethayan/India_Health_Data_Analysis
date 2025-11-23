from flask import Flask, render_template, request
from data import load_all_data

app = Flask(__name__)

dataframes = load_all_data()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
