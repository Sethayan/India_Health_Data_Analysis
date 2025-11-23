from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load Excel file
    df=pd.read_csv('data/Life_expectency_after_birth.csv',skiprows=4)
    df_mmr=pd.read_csv('data/MMR.csv',skiprows=4)
    df_imr=pd.read_csv('data/IMR.csv',skiprows=4)
    
    # Filter for India
    india_df = df[df['Country Name'] == 'India']
    indian_mmr = df_mmr[df_mmr['Country Name'] == 'India']
    indian_imr = df_imr[df_imr['Country Name'] == 'India']

    # Transpose years to columns
     # Extract year columns dynamically
    years = [col for col in india_df.columns[29:68] if col.isdigit()]
    life_exp = india_df[years].fillna(0).astype(float).values.flatten().tolist()
    imr_list = indian_imr[years].fillna(0).astype(float).values.flatten().tolist()
    mmr_list = indian_mmr[years].fillna(0).astype(float).values.flatten().tolist()

    return render_template('index.html', years=years, life_exp=life_exp,infant_mortality=imr_list,maternal_mortality=mmr_list)

@app.route('/country/')
def country(name=None):
    physicians = pd.read_csv('data/API_SH.MED.PHYS.ZS_DS2_en_csv_v2_10977.csv')
    #preprocessing
    physicians = physicians.drop(['Country Name','Indicator Name','Indicator Code'],axis=1)
    physicians = physicians[physicians['Country Code'] =='IND']
    physicians = physicians.set_index('Country Code').T
    physicians = physicians.dropna()
    years = physicians.index.to_list()
    values = physicians['IND'].to_list()
    physicians['% change'] = physicians['IND'].pct_change()
    avg_change = physicians['% change'].mean()*100

    return render_template('country_level.html', years=years,values = values,avg_change =avg_change)

@app.route('/state/')
def state(name=None):
    data = pd.read_csv('data/RS_Session_257_AU_282_1.csv')
    #preprocessing
    states = data['State/UT'].to_list()
    state_data = {}

    return render_template('state_level.html',states = states,state_data= state_data)

@app.route('/state/<state>')
def state_data(state):
    data = pd.read_csv('data/RS_Session_257_AU_282_1.csv')
    #preprocessing
    data = data[data['State/UT'] == state]
    data = data.dropna()
    print(data.to_string())
    data = data.drop(['State/UT','S. No.'],axis = 1).iloc[0].to_dict()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
