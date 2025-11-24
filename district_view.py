import pandas as pd

def get_district_data(dataframes,state_name=None):
    if 'district_wise_infra' not in dataframes or dataframes['district_wise_infra'].empty:
        return {'states': [], 'districts': []}
    
    df = dataframes['district_wise_infra'].copy()
    
    df.columns = [col.replace('\n', ' ').replace('\r', '').strip() for col in df.columns]
    
    state_col = 'States/Union Territory'
    district_col = 'Name of the District'
    
    df[state_col] = df[state_col].str.replace('\n', ' ').str.replace('\r', '').str.strip()
    df[state_col] = df[state_col].str.replace(r'\s+', ' ', regex=True)
    
    states = sorted(df[state_col].unique().tolist())
    
    if state_name:
        df = df[df[state_col] == state_name]
    
    districts = []
    for _, row in df.iterrows():
        districts.append({
            'state': row[state_col],
            'district': row[district_col],
            'sc_rural': int(row['Sub Centres Rural']) if pd.notna(row['Sub Centres Rural']) else 0,
            'sc_urban': int(row['Sub Centres Urban']) if pd.notna(row['Sub Centres Urban']) else 0,
            'phc_rural': int(row['PHCs Rural']) if pd.notna(row['PHCs Rural']) else 0,
            'phc_urban': int(row['PHCs Urban']) if pd.notna(row['PHCs Urban']) else 0,
            'chc_rural': int(row['CHCs Rural']) if pd.notna(row['CHCs Rural']) else 0,
            'chc_urban': int(row['CHCs Urban']) if pd.notna(row['CHCs Urban']) else 0,
            'sdh': int(row['Sub Divisional Hospital']) if pd.notna(row['Sub Divisional Hospital']) else 0,
            'dh': int(row['District Hospital']) if pd.notna(row['District Hospital']) else 0,
            'mc': int(row['Medical College']) if pd.notna(row['Medical College']) else 0,
        })
    
    return {'states': states, 'districts': districts}