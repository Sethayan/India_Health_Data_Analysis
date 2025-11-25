from database import get_db, models

def get_health_indicator():
    db = get_db()
    indicators = {}
    
    try:
        imr_data = db.query(models.IMR).all()
        if imr_data:
            indicators['imr'] = []
            for state in imr_data:
                indicators['imr'].append({
                    'State/UT': state.state_ut,
                    'IMR Total': state.imr_total,
                    'IMR Rural': state.imr_rural,
                    'IMR Urban': state.imr_urban
                })
        
        bd_data = db.query(models.BirthDeathRate).all()
        if bd_data:
            indicators['birth_death'] = []
            for state in bd_data:
                indicators['birth_death'].append({
                    'State/UT': state.state_ut,
                    'Birth Rate Total': state.birth_rate_total,
                    'Birth Rate Rural': state.birth_rate_rural,
                    'Birth Rate Urban': state.birth_rate_urban,
                    'Death Rate Total': state.death_rate_total,
                    'Death Rate Rural': state.death_rate_rural,
                    'Death Rate Urban': state.death_rate_urban
                })
        
        density_data = db.query(models.StateDensity).all()
        if density_data:
            indicators['density'] = []
            for state in density_data:
                indicators['density'].append({
                    'State/UT': state.state_ut,
                    'Population Density Rural': state.density_rural,
                    'Population Density Urban': state.density_urban,
                    'Population Density Total': state.density_total
                })
        
        return indicators
    finally:
        db.close()