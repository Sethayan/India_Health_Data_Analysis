from database import get_db, models

def get_district_data(state_name=None):
    db = get_db()
    
    try:
        states_query = db.query(models.DistrictWiseInfra.state_ut).distinct().all()
        states = sorted([state[0] for state in states_query])
        
        if state_name:
            district_data = db.query(models.DistrictWiseInfra).filter(
                models.DistrictWiseInfra.state_ut == state_name
            ).all()
        else:
            district_data = db.query(models.DistrictWiseInfra).all()
        
        districts = []
        for row in district_data:
            districts.append({
                'state': row.state_ut,
                'district': row.district_name,
                'sc_rural': row.sub_centres_rural,
                'sc_urban': row.sub_centres_urban,
                'phc_rural': row.phcs_rural,
                'phc_urban': row.phcs_urban,
                'chc_rural': row.chcs_rural,
                'chc_urban': row.chcs_urban,
                'sdh': row.sub_divisional_hospital,
                'dh': row.district_hospital,
                'mc': row.medical_college
            })
        
        return {
            'states': states,
            'districts': districts
        }
    finally:
        db.close()