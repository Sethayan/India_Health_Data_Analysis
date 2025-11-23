import pandas as pd

def get_national_stats(dataframes):
    stats = {}
    
    # Get population count
    if 'state_population' in dataframes and not dataframes['state_population'].empty:
        df = dataframes['state_population']
        stats['total_population_2023'] = int(df['Estimated Population 2023 Total'].sum())
        stats['rural_population_2023'] = int(df['Estimated Population 2023 Rural'].sum())
        stats['urban_population_2023'] = int(df['Estimated Population 2023 Urban'].sum())
        stats['rural_percentage'] = round(stats['rural_population_2023'] / stats['total_population_2023'] * 100, 1)

    # Provide overall count
    if 'sc_phc_chc_count' in dataframes and not dataframes['sc_phc_chc_count'].empty:
        df = dataframes['sc_phc_chc_count']
        stats['total_phcs'] = int(df['PHCs Rural'].sum() + df['PHCs Urban'].sum())
        stats['rural_phcs'] = int(df['PHCs Rural'].sum())
        stats['urban_phcs'] = int(df['PHCs Urban'].sum())
        
        stats['total_chcs'] = int(df['CHCs Rural'].sum() + df['CHCs Urban'].sum())
        stats['rural_chcs'] = int(df['CHCs Rural'].sum())
        stats['urban_chcs'] = int(df['CHCs Urban'].sum())

        stats['total_sub_centres'] = int(df['Sub centres Rural'].sum() + df['Sub centres Urban'].sum())
        stats['rural_sub_centres'] = int(df['Sub centres Rural'].sum())
        stats['urban_sub_centres'] = int(df['Sub centres Urban'].sum())
    
    # Infant mortality rate data
    if 'imr' in dataframes and not dataframes['imr'].empty:
        df = dataframes['imr']
        stats['avg_imr'] = round(df['IMR Total'].mean(), 1)
        stats['avg_imr_rural'] = round(df['IMR Rural'].mean(), 1)
        stats['avg_imr_urban'] = round(df['IMR Urban'].mean(), 1)

    # Hospitals
    if 'sdh_dh_mc_count' in dataframes and not dataframes['sdh_dh_mc_count'].empty:
        df = dataframes['sdh_dh_mc_count']
        stats['total_dh'] = int(df['District Hospital (DH)'].sum())
        stats['total_sdh'] = int(df['Sub Divisional Hospital (SDH)'].sum())
        stats['total_medical_colleges'] = int(df['Medical Colleges'].sum())

    # Doctor count
    if 'mo_phc_rural' in dataframes and not dataframes['mo_phc_rural'].empty:
        df = dataframes['mo_phc_rural']
        stats['total_doctors_required_2023'] = int(df['Required 2023'].sum())
        stats['total_doctors_position_2023'] = int(df['In Position 2023'].sum())
        stats['total_doctors_vacant_2023'] = int(df['Vacant 2023'].sum())
    
    # Specialist Count
    if 'specialist_chc_rural' in dataframes and not dataframes['specialist_chc_rural'].empty:
        df = dataframes['specialist_chc_rural']
        stats['total_specialists_required_2023'] = int(df['Required 2023'].sum())
        stats['total_specialists_position_2023'] = int(df['In Position 2023'].sum())
        stats['total_specialists_vacant_2023'] = int(df['Vacant 2023'].sum())

    # Average Birth/Death rates
    if 'birth_death_rate' in dataframes and not dataframes['birth_death_rate'].empty:
        df = dataframes['birth_death_rate']
        stats['avg_birth_rate'] = round(df['Birth Rate Total'].mean(), 1)
        stats['avg_death_rate'] = round(df['Death Rate Total'].mean(), 1)
    
    return stats