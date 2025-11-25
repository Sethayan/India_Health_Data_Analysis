from database import get_db, models

def get_state_stats(state_name):
    db = get_db()
    stats = {'state_name': state_name}
    try:
        infra = db.query(models.StateWiseSCPHCCHCCount).filter(
            models.StateWiseSCPHCCHCCount.state_ut == state_name
        ).first()
        if infra:
            stats['sub_centres_rural'] = infra.sub_centres_rural
            stats['sub_centres_urban'] = infra.sub_centres_urban
            stats['phcs_rural'] = infra.phcs_rural
            stats['phcs_urban'] = infra.phcs_urban
            stats['chcs_rural'] = infra.chcs_rural
            stats['chcs_urban'] = infra.chcs_urban
            stats['total_sub_centres'] = stats['sub_centres_rural'] + stats['sub_centres_urban']
            stats['total_phcs'] = stats['phcs_rural'] + stats['phcs_urban']
            stats['total_chcs'] = stats['chcs_rural'] + stats['chcs_urban']
        
        hospitals = db.query(models.StateWiseSDHDHMCCount).filter(
            models.StateWiseSDHDHMCCount.state_ut == state_name
        ).first()
        if hospitals:
            stats['sdh'] = hospitals.sub_divisional_hospital
            stats['dh'] = hospitals.district_hospital
            stats['medical_colleges'] = hospitals.medical_colleges
        
        population = db.query(models.StatePopulation).filter(
            models.StatePopulation.state_ut == state_name
        ).first()
        if population:
            stats['population_2023'] = population.pop_2023_total
            stats['population_rural'] = population.pop_2023_rural
            stats['population_urban'] = population.pop_2023_urban
            stats['rural_percentage'] = population.pop_2023_rural_pct
        
        area = db.query(models.StateArea).filter(
            models.StateArea.state_ut == state_name
        ).first()
        if area:
            stats['total_area'] = area.total_area_sq_km
            stats['rural_area'] = area.rural_area_sq_km
            stats['districts'] = area.number_of_districts
            stats['villages'] = area.number_of_villages
        
        density = db.query(models.StateDensity).filter(
            models.StateDensity.state_ut == state_name
        ).first()
        if density:
            stats['density_total'] = density.density_total
            stats['density_rural'] = density.density_rural
            stats['density_urban'] = density.density_urban
        
        imr = db.query(models.IMR).filter(
            models.IMR.state_ut == state_name
        ).first()
        
        if imr:
            stats['imr_total'] = imr.imr_total
            stats['imr_rural'] = imr.imr_rural
            stats['imr_urban'] = imr.imr_urban
        
        bd_rate = db.query(models.BirthDeathRate).filter(
            models.BirthDeathRate.state_ut == state_name
        ).first()
        if bd_rate:
            stats['birth_rate'] = bd_rate.birth_rate_total
            stats['death_rate'] = bd_rate.death_rate_total
            stats['birth_rate_rural'] = bd_rate.birth_rate_rural
            stats['death_rate_rural'] = bd_rate.death_rate_rural
        
        shortfall = db.query(models.Shortfall).filter(
            models.Shortfall.state_ut == state_name
        ).first()
        if shortfall:
            stats['sc_shortfall_pct'] = shortfall.sc_shortfall_pct
            stats['phc_shortfall_pct'] = shortfall.phc_shortfall_pct
            stats['chc_shortfall_pct'] = shortfall.chc_shortfall_pct
        
        return stats
    finally:
        db.close()

def get_state_comparison_data(state_name):
    db = get_db()
    comparison = {}
    
    try:
        infra = db.query(models.FunctionInfraRural).filter(
            models.FunctionInfraRural.state_ut == state_name
        ).first()
        if infra:
            comparison['infra'] = {
                'sc_2005': infra.sub_centre_2005,
                'sc_2023': infra.sub_centre_2023,
                'phc_2005': infra.phcs_2005,
                'phc_2023': infra.phcs_2023,
                'chc_2005': infra.chcs_2005,
                'chc_2023': infra.chcs_2023,
            }
        
        return comparison
    finally:
        db.close()

def get_state_list_data():
    db = get_db()
    try:
        states = db.query(models.StateWiseSCPHCCHCCount.state_ut).all()
        state_list = []
        for state in states:
            state_list.append(state[0])
        
        return state_list
    finally:
        db.close()