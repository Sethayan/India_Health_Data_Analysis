import pandas as pd

def get_national_stats(dataframes):
    stats = {}
    
    if 'state_population' in dataframes and not dataframes['state_population'].empty:
        df = dataframes['state_population']
        stats['total_population_2023'] = int(df['Estimated Population 2023 Total'].sum())
        stats['rural_population_2023'] = int(df['Estimated Population 2023 Rural'].sum())
        stats['urban_population_2023'] = int(df['Estimated Population 2023 Urban'].sum())
        stats['rural_percentage'] = round(stats['rural_population_2023'] / stats['total_population_2023'] * 100, 1)

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
    
    if 'imr' in dataframes and not dataframes['imr'].empty:
        df = dataframes['imr']
        stats['avg_imr'] = round(df['IMR Total'].mean(), 1)
        stats['avg_imr_rural'] = round(df['IMR Rural'].mean(), 1)
        stats['avg_imr_urban'] = round(df['IMR Urban'].mean(), 1)

    if 'sdh_dh_mc_count' in dataframes and not dataframes['sdh_dh_mc_count'].empty:
        df = dataframes['sdh_dh_mc_count']
        stats['total_dh'] = int(df['District Hospital (DH)'].sum())
        stats['total_sdh'] = int(df['Sub Divisional Hospital (SDH)'].sum())
        stats['total_medical_colleges'] = int(df['Medical Colleges'].sum())

    if 'mo_phc_rural' in dataframes and not dataframes['mo_phc_rural'].empty:
        df = dataframes['mo_phc_rural']
        stats['total_doctors_required_2023'] = int(df['Required 2023'].sum())
        stats['total_doctors_position_2023'] = int(df['In Position 2023'].sum())
        stats['total_doctors_vacant_2023'] = int(df['Vacant 2023'].sum())
    
    if 'specialist_chc_rural' in dataframes and not dataframes['specialist_chc_rural'].empty:
        df = dataframes['specialist_chc_rural']
        stats['total_specialists_required_2023'] = int(df['Required 2023'].sum())
        stats['total_specialists_position_2023'] = int(df['In Position 2023'].sum())
        stats['total_specialists_vacant_2023'] = int(df['Vacant 2023'].sum())

    if 'birth_death_rate' in dataframes and not dataframes['birth_death_rate'].empty:
        df = dataframes['birth_death_rate']
        stats['avg_birth_rate'] = round(df['Birth Rate Total'].mean(), 1)
        stats['avg_death_rate'] = round(df['Death Rate Total'].mean(), 1)
    
    if 'shortfall' in dataframes and not dataframes['shortfall'].empty:
        df = dataframes['shortfall']
        stats['avg_sc_shortfall'] = round(df['Sub Centres % Shortfall'].mean(), 1)
        stats['avg_phc_shortfall'] = round(df['PHCs % Shortfall'].mean(), 1)
        stats['avg_chc_shortfall'] = round(df['CHCs % Shortfall'].mean(), 1)
        
        stats['total_sc_shortfall'] = int(df['Sub Centres S'].sum())
        stats['total_phc_shortfall'] = int(df['PHCs S'].sum())
        stats['total_chc_shortfall'] = int(df['CHCs S'].sum())

    return stats

def get_insights(dataframes):
    insights = []
    
    if 'shortfall' in dataframes and not dataframes['shortfall'].empty:
        df = dataframes['shortfall'].copy()
        df['PHCs % Shortfall'] = pd.to_numeric(df['PHCs % Shortfall'])
        if not df.empty:
            max_idx = df['PHCs % Shortfall'].idxmax()
            if df.loc[max_idx, 'PHCs % Shortfall'] > 0:
                insights.append({
                    'type': 'critical',
                    'icon': 'fa-exclamation-triangle',
                    'title': 'Highest PHC Shortfall',
                    'value': f"{df.loc[max_idx, 'PHCs % Shortfall']:.0f}%",
                    'description': f"{df.loc[max_idx, 'State/UT']} has the highest PHC shortfall at {df.loc[max_idx, 'PHCs % Shortfall']:.0f}%"
                })
        
        df['CHCs % Shortfall'] = pd.to_numeric(df['CHCs % Shortfall'])
        if not df.empty:
            max_idx = df['CHCs % Shortfall'].idxmax()
            if df.loc[max_idx, 'CHCs % Shortfall'] > 0:
                insights.append({
                    'type': 'critical',
                    'icon': 'fa-hospital-o',
                    'title': 'Highest CHC Shortfall',
                    'value': f"{df.loc[max_idx, 'CHCs % Shortfall']:.0f}%",
                    'description': f"{df.loc[max_idx, 'State/UT']} has the highest CHC shortfall at {df.loc[max_idx, 'CHCs % Shortfall']:.0f}%"
                })
        
        df['Sub Centres % Shortfall'] = pd.to_numeric(df['Sub Centres % Shortfall'])
        if not df.empty:
            max_idx = df['Sub Centres % Shortfall'].idxmax()
            if df.loc[max_idx, 'Sub Centres % Shortfall'] > 0:
                insights.append({
                    'type': 'warning',
                    'icon': 'fa-building',
                    'title': 'Highest Sub Centre Shortfall',
                    'value': f"{df.loc[max_idx, 'Sub Centres % Shortfall']:.0f}%",
                    'description': f"{df.loc[max_idx, 'State/UT']} has the highest Sub Centres shortfall at {df.loc[max_idx, 'Sub Centres % Shortfall']:.0f}%"
                })
    
    if 'imr' in dataframes and not dataframes['imr'].empty:
        df = dataframes['imr'].copy()
        max_idx = df['IMR Total'].idxmax()
        insights.append({
            'type': 'critical',
            'icon': 'fa-child',
            'title': 'Highest Infant Mortality',
            'value': f"{df.loc[max_idx, 'IMR Total']} per 1000",
            'description': f"{df.loc[max_idx, 'State/UT']} has IMR of {df.loc[max_idx, 'IMR Total']} per 1000 live births"
        })
        
        min_idx = df['IMR Total'].idxmin()
        insights.append({
            'type': 'success',
            'icon': 'fa-thumbs-up',
            'title': 'Lowest Infant Mortality',
            'value': f"{df.loc[min_idx, 'IMR Total']} per 1000",
            'description': f"{df.loc[min_idx, 'State/UT']} has the lowest IMR of {df.loc[min_idx, 'IMR Total']}"
        })
    
    if 'function_infra_rural' in dataframes and not dataframes['function_infra_rural'].empty:
        df = dataframes['function_infra_rural'].copy()
       
        df['PHC_Growth'] = ((df['PHCs 2023'] - df['PHCs 2005']) / df['PHCs 2005'].replace(0, 1)) * 100
        df['CHC_Growth'] = ((df['CHCs 2023'] - df['CHCs 2005']) / df['CHCs 2005'].replace(0, 1)) * 100
        
        max_phc_idx = df['PHC_Growth'].idxmax()
        if df.loc[max_phc_idx, 'PHC_Growth'] > 0:
            insights.append({
                'type': 'success',
                'icon': 'fa-line-chart',
                'title': 'Highest PHC Growth (2005-2023)',
                'value': f"+{df.loc[max_phc_idx, 'PHC_Growth']:.0f}%",
                'description': f"{df.loc[max_phc_idx, 'State/UT']} achieved {df.loc[max_phc_idx, 'PHC_Growth']:.0f}% growth in PHCs"
            })
        
        max_chc_idx = df['CHC_Growth'].idxmax()
        if df.loc[max_chc_idx, 'CHC_Growth'] > 0:
            insights.append({
                'type': 'success',
                'icon': 'fa-area-chart',
                'title': 'Highest CHC Growth (2005-2023)',
                'value': f"+{df.loc[max_chc_idx, 'CHC_Growth']:.0f}%",
                'description': f"{df.loc[max_chc_idx, 'State/UT']} achieved {df.loc[max_chc_idx, 'CHC_Growth']:.0f}% growth in CHCs"
            })
    
    if 'mo_phc_rural' in dataframes and not dataframes['mo_phc_rural'].empty:
        df = dataframes['mo_phc_rural'].copy()
        df['Vacant 2023'] = pd.to_numeric(df['Vacant 2023']).fillna(0)
        df['Vacancy_Rate'] = (df['Vacant 2023'] / df['Sanctioned 2023'].replace(0, 1)) * 100
        
        max_idx = df['Vacancy_Rate'].idxmax()
        if df.loc[max_idx, 'Vacancy_Rate'] > 0:
            insights.append({
                'type': 'warning',
                'icon': 'fa-user-md',
                'title': 'Highest Doctor Vacancy Rate',
                'value': f"{df.loc[max_idx, 'Vacancy_Rate']:.0f}%",
                'description': f"{df.loc[max_idx, 'State/UT']} has {df.loc[max_idx, 'Vacancy_Rate']:.0f}% doctor vacancies in PHCs"
            })
    
    if 'specialist_chc_rural' in dataframes and not dataframes['specialist_chc_rural'].empty:
        df = dataframes['specialist_chc_rural'].copy()
        df['Shortfall 2023'] = pd.to_numeric(df['Shortfall 2023'].replace('-', 0), errors='coerce').fillna(0)
        total_shortfall = df['Shortfall 2023'].sum()
        if total_shortfall > 0:
            insights.append({
                'type': 'critical',
                'icon': 'fa-stethoscope',
                'title': 'National Specialist Shortfall',
                'value': f"{int(total_shortfall):,}",
                'description': f"India faces a shortfall of {int(total_shortfall):,} specialists at CHCs"
            })
    
    return insights

def get_overview_ranking(dataframes):
    rankings = {}
    
    if 'imr' in dataframes and not dataframes['imr'].empty:
        df = dataframes['imr'].copy()
        df_sorted = df.sort_values('IMR Total')
        rankings['imr_best'] = df_sorted.head(5)[['State/UT', 'IMR Total']].to_dict('records')
        rankings['imr_worst'] = df_sorted.tail(5)[['State/UT', 'IMR Total']].to_dict('records')[::-1]
    
    if 'shortfall' in dataframes and not dataframes['shortfall'].empty:
        df = dataframes['shortfall'].copy()
        df['PHCs % Shortfall'] = pd.to_numeric(df['PHCs % Shortfall'])
        df_sorted = df.sort_values('PHCs % Shortfall', ascending=False)
        rankings['phc_shortfall_worst'] = df_sorted[df_sorted['PHCs % Shortfall'] > 0].head(5)[['State/UT', 'PHCs % Shortfall']].to_dict('records')
    
    return rankings

def get_shortfall(dataframes):

    if 'shortfall' not in dataframes or dataframes['shortfall'].empty:
        return {}
    
    df = dataframes['shortfall'].copy()
    
    for col in ['Sub Centres % Shortfall', 'PHCs % Shortfall', 'CHCs % Shortfall']:
        df[col] = pd.to_numeric(df[col])
    
    return {
        'labels': df['State/UT'].tolist(),
        'sc_shortfall': df['Sub Centres % Shortfall'].tolist(),
        'phc_shortfall': df['PHCs % Shortfall'].tolist(),
        'chc_shortfall': df['CHCs % Shortfall'].tolist(),
        'sc_required': df['Sub Centres R'].tolist(),
        'sc_present': df['Sub Centres P'].tolist(),
        'phc_required': df['PHCs R'].tolist(),
        'phc_present': df['PHCs P'].tolist(),
        'chc_required': df['CHCs R'].tolist(),
        'chc_present': df['CHCs P'].tolist(),
    }