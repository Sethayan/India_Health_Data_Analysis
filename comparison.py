import pandas as pd

def get_comparison_data(dataframes):
    data = {}
    
    
    if 'function_infra_rural' in dataframes and not dataframes['function_infra_rural'].empty:
        df = dataframes['function_infra_rural']
        data['infra_comparison'] = {
            'labels': df['State/UT'].tolist(),
            'sc_2005': df['Sub Centre 2005'].tolist(),
            'sc_2023': df['Sub Centre 2023'].tolist(),
            'phc_2005': df['PHCs 2005'].tolist(),
            'phc_2023': df['PHCs 2023'].tolist(),
            'chc_2005': df['CHCs 2005'].tolist(),
            'chc_2023': df['CHCs 2023'].tolist()
        }
    
    
    if 'mo_phc_rural' in dataframes and not dataframes['mo_phc_rural'].empty:
        df = dataframes['mo_phc_rural'].copy()
        df['In Position 2005'] = pd.to_numeric(df['In Position 2005'])
        df['In Position 2023'] = pd.to_numeric(df['In Position 2023'])
        data['doctors_comparison'] = {
            'labels': df['State/UT'].tolist(),
            'position_2005': df['In Position 2005'].tolist(),
            'position_2023': df['In Position 2023'].tolist(),
            'required_2005': df['Required 2005'].tolist(),
            'required_2023': df['Required 2023'].tolist(),
        }
    
    
    if 'specialist_chc_rural' in dataframes and not dataframes['specialist_chc_rural'].empty:
        df = dataframes['specialist_chc_rural'].copy()
        df['In Position 2005'] = pd.to_numeric(df['In Position 2005'])
        df['In Position 2023'] = pd.to_numeric(df['In Position 2023'])
        data['specialists_comparison'] = {
            'labels': df['State/UT'].tolist(),
            'position_2005': df['In Position 2005'].tolist(),
            'position_2023': df['In Position 2023'].tolist(),
        }
    
    return data