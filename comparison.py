from database import get_db, models

def get_comparison_data():
    db = get_db()
    data = {}
    
    try:
        infra_data = db.query(models.FunctionInfraRural).all()
        if infra_data:
            labels = []
            sc_2005 = []
            sc_2023 = []
            phc_2005 = []
            phc_2023 = []
            chc_2005 = []
            chc_2023 = []
            
            for state in infra_data:
                labels.append(state.state_ut)
                sc_2005.append(state.sub_centre_2005)
                sc_2023.append(state.sub_centre_2023)
                phc_2005.append(state.phcs_2005)
                phc_2023.append(state.phcs_2023)
                chc_2005.append(state.chcs_2005)
                chc_2023.append(state.chcs_2023)
            
            data['infra_comparison'] = {
                'labels': labels,
                'sc_2005': sc_2005,
                'sc_2023': sc_2023,
                'phc_2005': phc_2005,
                'phc_2023': phc_2023,
                'chc_2005': chc_2005,
                'chc_2023': chc_2023
            }
        
        doctors_data = db.query(models.MOPHCRural).all()
        if doctors_data:
            labels = []
            position_2005 = []
            position_2023 = []
            required_2005 = []
            required_2023 = []
            
            for state in doctors_data:
                labels.append(state.state_ut)
                position_2005.append(state.in_position_2005)
                position_2023.append(state.in_position_2023)
                required_2005.append(state.required_2005)
                required_2023.append(state.required_2023)
            
            data['doctors_comparison'] = {
                'labels': labels,
                'position_2005': position_2005,
                'position_2023': position_2023,
                'required_2005': required_2005,
                'required_2023': required_2023,
            }
        
        specialists_data = db.query(models.SpecialistCHCRural).all()
        if specialists_data:
            labels = []
            position_2005 = []
            position_2023 = []
            
            for state in specialists_data:
                labels.append(state.state_ut)
                position_2005.append(state.in_position_2005)
                position_2023.append(state.in_position_2023)
            
            data['specialists_comparison'] = {
                'labels': labels,
                'position_2005': position_2005,
                'position_2023': position_2023,
            }
        return data
    finally:
        db.close()


def get_yearly_comparison():
    db = get_db()
    data = {}
    try:
        function_data = db.query(models.FunctionSCPHCCHCRural).all()
        if function_data:
            labels = []
            sc_2022 = []
            sc_2023 = []
            phc_2022 = []
            phc_2023 = []
            chc_2022 = []
            chc_2023 = []
            
            for state in function_data:
                labels.append(state.state_ut)
                sc_2022.append(state.sub_centre_march_2022)
                sc_2023.append(state.sub_centre_march_2023)
                phc_2022.append(state.phcs_march_2022)
                phc_2023.append(state.phcs_march_2023)
                chc_2022.append(state.chcs_march_2022)
                chc_2023.append(state.chcs_march_2023)
            
            data['function_2022_2023'] = {
                'labels': labels,
                'sc_2022': sc_2022,
                'sc_2023': sc_2023,
                'phc_2022': phc_2022,
                'phc_2023': phc_2023,
                'chc_2022': chc_2022,
                'chc_2023': chc_2023,
            }
        
        manpower_data = db.query(models.ManpowerPart1).all()
        if manpower_data:
            labels = []
            doctors_2022 = []
            doctors_2023 = []
            specialists_2022 = []
            specialists_2023 = []
            
            for state in manpower_data:
                labels.append(state.state_ut)
                doctors_2022.append(state.doctors_phc_march_2022)
                doctors_2023.append(state.doctors_phc_march_2023)
                specialists_2022.append(state.specialists_chc_march_2022)
                specialists_2023.append(state.specialists_chc_march_2023)
            
            data['manpower_2022_2023'] = {
                'labels': labels,
                'doctors_2022': doctors_2022,
                'doctors_2023': doctors_2023,
                'specialists_2022': specialists_2022,
                'specialists_2023': specialists_2023,
            }
        return data
    finally:
        db.close()