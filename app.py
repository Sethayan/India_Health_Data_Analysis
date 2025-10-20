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

if __name__ == '__main__':
    app.run(debug=True)
