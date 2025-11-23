import os
import pandas as pd

DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')

def load_all_data():
    """Load all data"""
    dataframes = {}

    csv_files = {
        'sc_phc_chc_count': 'State Wise SC_PHC_CHC Count.csv',
        'sdh_dh_mc_count': 'State Wise SDH_DH_MC Count.csv',
        'function_infra_rural': 'Function Infra Rural (CS1).csv',
        'building_sc_rural': 'Building Position SC Rural (CS2).csv',
        'building_phc_rural': 'Building Position PHC Rural (CS3).csv',
        'building_chc_rural': 'Building Position CHC Rural (CS4).csv',
        'mo_phc_rural': 'MO at PHC Rural (CS5).csv',
        'specialist_chc_rural': 'Specialist at CHC Rural (CS6).csv',
        'radiographers_chc_rural': 'Radiographers at CHC Rural (CS7).csv',
        'pharmacist_rural': 'Pharamacist at CHC PHC Rural (CS8).csv',
        'lab_tech_rural': 'Lab Tech at CHC PHC Rural (CS9).csv',
        'nursing_rural': 'Nursing at CHC PHC Rural (CS10).csv',
        'function_sc_phc_chc_rural': 'Function SC PHC CHS Rural (CS11).csv',
        'building_position_2022_2023': 'Building Position SC PHC CHC (CS12).csv',
        'manpower_part1': 'Manpower position SC PHC (CS13).csv',
        'manpower_part2': 'Manpower position SC PHC (CS14).csv',
        'district_wise_infra': 'District Wise Infra.csv',
        'state_area': 'State Wise Area (115).csv',
        'state_population': 'State Wise Population (116).csv',
        'state_density': 'State Wise Population Density (117).csv',
        'birth_death_rate': 'State Wise Birth Death Rate (118).csv',
        'imr': 'State Wise Infant Mortality Rate (119).csv',
        'shortfall': 'Shortfall health facilities.csv',
        'building_sc_position': 'State wise building position SC rural.csv',
        'building_phc_position': 'State wise building position PHC rural.csv',
        'building_chc_position': 'State wise building position CHC rural.csv',
    }
    
    for key, filename in csv_files.items():
        filepath = os.path.join(DATA_DIRECTORY, filename)
        if os.path.exists(filepath):
            try:
                df = pd.read_csv(filepath, encoding='utf-8')
                dataframes[key] = df
            except Exception as e:
                print(f"Error loading {filename}: {e}")
                dataframes[key] = pd.DataFrame()
        else:
            print(f"File not found: {filename}")
            dataframes[key] = pd.DataFrame()
    
    return dataframes
