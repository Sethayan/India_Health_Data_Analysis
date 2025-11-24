def get_state_stats(state_name,dataframes):

    stats = {'state_name': state_name}
    
    df = dataframes['sc_phc_chc_count']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['sub_centres_rural'] = int(row['Sub centres Rural'])
        stats['sub_centres_urban'] = int(row['Sub centres Urban'])
        stats['phcs_rural'] = int(row['PHCs Rural'])
        stats['phcs_urban'] = int(row['PHCs Urban'])
        stats['chcs_rural'] = int(row['CHCs Rural'])
        stats['chcs_urban'] = int(row['CHCs Urban'])
        stats['total_sub_centres'] = stats['sub_centres_rural'] + stats['sub_centres_urban']
        stats['total_phcs'] = stats['phcs_rural'] + stats['phcs_urban']
        stats['total_chcs'] = stats['chcs_rural'] + stats['chcs_urban']

    df = dataframes['sdh_dh_mc_count']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['sdh'] = int(row['Sub Divisional Hospital (SDH)'])
        stats['dh'] = int(row['District Hospital (DH)'])
        stats['medical_colleges'] = int(row['Medical Colleges'])
    
    df = dataframes['state_population']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['population_2023'] = int(row['Estimated Population 2023 Total'])
        stats['population_rural'] = int(row['Estimated Population 2023 Rural'])
        stats['population_urban'] = int(row['Estimated Population 2023 Urban'])
        stats['rural_percentage'] = float(row['Estimated Population 2023 Rural %'])
        
    df = dataframes['state_area']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['total_area'] = float(row['Total Area (Sq. Km.)'])
        stats['rural_area'] = float(row['Rural Area (Sq. Km.)'])
        stats['districts'] = int(row['Number of Districts'])
        stats['villages'] = int(row['Number of Villages'])
    
    df = dataframes['state_density']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['density_total'] = int(row['Population Density Total'])
        stats['density_rural'] = int(row['Population Density Rural'])
        stats['density_urban'] = int(row['Population Density Urban'])
    
    df = dataframes['imr']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['imr_total'] = int(row['IMR Total'])
        stats['imr_rural'] = int(row['IMR Rural'])
        stats['imr_urban'] = int(row['IMR Urban'])    
    
    df = dataframes['birth_death_rate']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['birth_rate'] = float(row['Birth Rate Total'])
        stats['death_rate'] = float(row['Death Rate Total'])
        stats['birth_rate_rural'] = float(row['Birth Rate Rural'])
        stats['death_rate_rural'] = float(row['Death Rate Rural'])
    
    df = dataframes['shortfall']
    state_data = df[df['State/UT'] == state_name]
    if not state_data.empty:
        row = state_data.iloc[0]
        stats['sc_shortfall_pct'] = row['Sub Centres % Shortfall'] 
        stats['phc_shortfall_pct'] = row['PHCs % Shortfall'] 
        stats['chc_shortfall_pct'] = row['CHCs % Shortfall']
    
    return stats