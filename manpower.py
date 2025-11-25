from database import get_db, models

def get_manpower_data():
    db = get_db()
    manpower_data = {}
    try:
        doctors_data = db.query(models.MOPHCRural).all()
        if doctors_data:
            manpower_data['doctors'] = []
            for state in doctors_data:
                manpower_data['doctors'].append({
                    'State/UT': state.state_ut,
                    'Required 2005': state.required_2005,
                    'Sanctioned 2005': state.sanctioned_2005,
                    'In Position 2005': state.in_position_2005,
                    'Vacant 2005': state.vacant_2005,
                    'Shortfall 2005': state.shortfall_2005,
                    'Required 2023': state.required_2023,
                    'Sanctioned 2023': state.sanctioned_2023,
                    'In Position 2023': state.in_position_2023,
                    'Vacant 2023': state.vacant_2023,
                    'Shortfall 2023': state.shortfall_2023
                })
        
        specialists_data = db.query(models.SpecialistCHCRural).all()
        if specialists_data:
            manpower_data['specialists'] = []
            for state in specialists_data:
                manpower_data['specialists'].append({
                    'State/UT': state.state_ut,
                    'Required 2005': state.required_2005,
                    'Sanctioned 2005': state.sanctioned_2005,
                    'In Position 2005': state.in_position_2005,
                    'Vacant 2005': state.vacant_2005,
                    'Shortfall 2005': state.shortfall_2005,
                    'Required 2023': state.required_2023,
                    'Sanctioned 2023': state.sanctioned_2023,
                    'In Position 2023': state.in_position_2023,
                    'Vacant 2023': state.vacant_2023,
                    'Shortfall 2023': state.shortfall_2023
                })
        
        nursing_data = db.query(models.NursingRural).all()
        if nursing_data:
            manpower_data['nursing'] = []
            for state in nursing_data:
                manpower_data['nursing'].append({
                    'State/UT': state.state_ut,
                    'Required 2005': state.required_2005,
                    'Sanctioned 2005': state.sanctioned_2005,
                    'In Position 2005': state.in_position_2005,
                    'Vacant 2005': state.vacant_2005,
                    'Shortfall 2005': state.shortfall_2005,
                    'Required 2023': state.required_2023,
                    'Sanctioned 2023': state.sanctioned_2023,
                    'In Position 2023': state.in_position_2023,
                    'Vacant 2023': state.vacant_2023,
                    'Shortfall 2023': state.shortfall_2023
                })
        
        pharmacists_data = db.query(models.PharmacistRural).all()
        if pharmacists_data:
            manpower_data['pharmacists'] = []
            for state in pharmacists_data:
                manpower_data['pharmacists'].append({
                    'State/UT': state.state_ut,
                    'Required 2005': state.required_2005,
                    'Sanctioned 2005': state.sanctioned_2005,
                    'In Position 2005': state.in_position_2005,
                    'Vacant 2005': state.vacant_2005,
                    'Shortfall 2005': state.shortfall_2005,
                    'Required 2023': state.required_2023,
                    'Sanctioned 2023': state.sanctioned_2023,
                    'In Position 2023': state.in_position_2023,
                    'Vacant 2023': state.vacant_2023,
                    'Shortfall 2023': state.shortfall_2023
                })
        
        return manpower_data
    finally:
        db.close()