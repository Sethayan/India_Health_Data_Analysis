from database import get_db, models
from sqlalchemy import func

def get_national_stats():
    db = get_db()
    stats = {}
    
    try:
        pop_data = db.query(
            func.sum(models.StatePopulation.pop_2023_total).label('total'),
            func.sum(models.StatePopulation.pop_2023_rural).label('rural'),
            func.sum(models.StatePopulation.pop_2023_urban).label('urban')
        ).first()
        
        if pop_data and pop_data.total:
            stats['total_population_2023'] = int(pop_data.total)
            stats['rural_population_2023'] = int(pop_data.rural)
            stats['urban_population_2023'] = int(pop_data.urban)
            stats['rural_percentage'] = round(stats['rural_population_2023'] / stats['total_population_2023'] * 100, 1)
        
        infra_data = db.query(
            func.sum(models.StateWiseSCPHCCHCCount.phcs_rural).label('phcs_rural'),
            func.sum(models.StateWiseSCPHCCHCCount.phcs_urban).label('phcs_urban'),
            func.sum(models.StateWiseSCPHCCHCCount.chcs_rural).label('chcs_rural'),
            func.sum(models.StateWiseSCPHCCHCCount.chcs_urban).label('chcs_urban'),
            func.sum(models.StateWiseSCPHCCHCCount.sub_centres_rural).label('sc_rural'),
            func.sum(models.StateWiseSCPHCCHCCount.sub_centres_urban).label('sc_urban')
        ).first()
        
        if infra_data:
            stats['total_phcs'] = int(infra_data.phcs_rural + infra_data.phcs_urban)
            stats['rural_phcs'] = int(infra_data.phcs_rural)
            stats['urban_phcs'] = int(infra_data.phcs_urban)
            
            stats['total_chcs'] = int(infra_data.chcs_rural + infra_data.chcs_urban)
            stats['rural_chcs'] = int(infra_data.chcs_rural)
            stats['urban_chcs'] = int(infra_data.chcs_urban)
            
            stats['total_sub_centres'] = int(infra_data.sc_rural + infra_data.sc_urban)
            stats['rural_sub_centres'] = int(infra_data.sc_rural)
            stats['urban_sub_centres'] = int(infra_data.sc_urban)
        
        imr_data = db.query(
            func.avg(models.IMR.imr_total).label('avg_total'),
            func.avg(models.IMR.imr_rural).label('avg_rural'),
            func.avg(models.IMR.imr_urban).label('avg_urban')
        ).first()
        
        if imr_data:
            stats['avg_imr'] = round(imr_data.avg_total, 1) if imr_data.avg_total else 0
            stats['avg_imr_rural'] = round(imr_data.avg_rural, 1) if imr_data.avg_rural else 0
            stats['avg_imr_urban'] = round(imr_data.avg_urban, 1) if imr_data.avg_urban else 0
        
        hospital_data = db.query(
            func.sum(models.StateWiseSDHDHMCCount.district_hospital).label('dh'),
            func.sum(models.StateWiseSDHDHMCCount.sub_divisional_hospital).label('sdh'),
            func.sum(models.StateWiseSDHDHMCCount.medical_colleges).label('mc')
        ).first()
        
        if hospital_data:
            stats['total_dh'] = int(hospital_data.dh)
            stats['total_sdh'] = int(hospital_data.sdh)
            stats['total_medical_colleges'] = int(hospital_data.mc)
        
        doctors_data = db.query(
            func.sum(models.MOPHCRural.required_2023).label('required'),
            func.sum(models.MOPHCRural.in_position_2023).label('position'),
            func.sum(models.MOPHCRural.vacant_2023).label('vacant')
        ).first()
        
        if doctors_data:
            stats['total_doctors_required_2023'] = int(doctors_data.required)
            stats['total_doctors_position_2023'] = int(doctors_data.position)
            stats['total_doctors_vacant_2023'] = int(doctors_data.vacant)
        
        specialists_data = db.query(
            func.sum(models.SpecialistCHCRural.required_2023).label('required'),
            func.sum(models.SpecialistCHCRural.in_position_2023).label('position'),
            func.sum(models.SpecialistCHCRural.vacant_2023).label('vacant')
        ).first()
        
        if specialists_data:
            stats['total_specialists_required_2023'] = int(specialists_data.required)
            stats['total_specialists_position_2023'] = int(specialists_data.position)
            stats['total_specialists_vacant_2023'] = int(specialists_data.vacant)
        
        bd_data = db.query(
            func.avg(models.BirthDeathRate.birth_rate_total).label('birth'),
            func.avg(models.BirthDeathRate.death_rate_total).label('death')
        ).first()
        
        if bd_data:
            stats['avg_birth_rate'] = round(bd_data.birth, 1) if bd_data.birth else 0
            stats['avg_death_rate'] = round(bd_data.death, 1) if bd_data.death else 0
        
        shortfall_data = db.query(
            func.avg(models.Shortfall.sc_shortfall_pct).label('sc_pct'),
            func.avg(models.Shortfall.phc_shortfall_pct).label('phc_pct'),
            func.avg(models.Shortfall.chc_shortfall_pct).label('chc_pct'),
            func.sum(models.Shortfall.sc_shortfall).label('sc_total'),
            func.sum(models.Shortfall.phc_shortfall).label('phc_total'),
            func.sum(models.Shortfall.chc_shortfall).label('chc_total')
        ).first()
        if shortfall_data:
            stats['avg_sc_shortfall'] = round(shortfall_data.sc_pct, 1) if shortfall_data.sc_pct else 0
            stats['avg_phc_shortfall'] = round(shortfall_data.phc_pct, 1) if shortfall_data.phc_pct else 0
            stats['avg_chc_shortfall'] = round(shortfall_data.chc_pct, 1) if shortfall_data.chc_pct else 0
            
            stats['total_sc_shortfall'] = int(shortfall_data.sc_total) if shortfall_data.sc_total else 0
            stats['total_phc_shortfall'] = int(shortfall_data.phc_total) if shortfall_data.phc_total else 0
            stats['total_chc_shortfall'] = int(shortfall_data.chc_total) if shortfall_data.chc_total else 0
        
        return stats
    finally:
        db.close()


def get_insights():
    db = get_db()
    insights = []
    
    try:
        phc_shortfall = db.query(models.Shortfall).filter(
            models.Shortfall.phc_shortfall_pct > 0
        ).order_by(models.Shortfall.phc_shortfall_pct.desc()).first()
        
        if phc_shortfall:
            insights.append({
                'type': 'critical',
                'icon': 'fa-exclamation-triangle',
                'title': 'Highest PHC Shortfall',
                'value': f"{phc_shortfall.phc_shortfall_pct:.0f}%",
                'description': f"{phc_shortfall.state_ut} has the highest PHC shortfall at {phc_shortfall.phc_shortfall_pct:.0f}%"
            })
        chc_shortfall = db.query(models.Shortfall).filter(
            models.Shortfall.chc_shortfall_pct > 0
        ).order_by(models.Shortfall.chc_shortfall_pct.desc()).first()
        
        if chc_shortfall:
            insights.append({
                'type': 'critical',
                'icon': 'fa-hospital-o',
                'title': 'Highest CHC Shortfall',
                'value': f"{chc_shortfall.chc_shortfall_pct:.0f}%",
                'description': f"{chc_shortfall.state_ut} has the highest CHC shortfall at {chc_shortfall.chc_shortfall_pct:.0f}%"
            })
        
        sc_shortfall = db.query(models.Shortfall).filter(
            models.Shortfall.sc_shortfall_pct > 0
        ).order_by(models.Shortfall.sc_shortfall_pct.desc()).first()
        
        if sc_shortfall:
            insights.append({
                'type': 'warning',
                'icon': 'fa-building',
                'title': 'Highest Sub Centre Shortfall',
                'value': f"{sc_shortfall.sc_shortfall_pct:.0f}%",
                'description': f"{sc_shortfall.state_ut} has the highest Sub Centres shortfall at {sc_shortfall.sc_shortfall_pct:.0f}%"
            })
        
        highest_imr = db.query(models.IMR).order_by(
            models.IMR.imr_total.desc()
        ).first()
        
        if highest_imr:
            insights.append({
                'type': 'critical',
                'icon': 'fa-child',
                'title': 'Highest Infant Mortality',
                'value': f"{highest_imr.imr_total} per 1000",
                'description': f"{highest_imr.state_ut} has IMR of {highest_imr.imr_total} per 1000 live births"
            })
        
        lowest_imr = db.query(models.IMR).order_by(
            models.IMR.imr_total.asc()
        ).first()
        if lowest_imr:
            insights.append({
                'type': 'success',
                'icon': 'fa-thumbs-up',
                'title': 'Lowest Infant Mortality',
                'value': f"{lowest_imr.imr_total} per 1000",
                'description': f"{lowest_imr.state_ut} has the lowest IMR of {lowest_imr.imr_total}"
            })
        
        growth_data = db.query(models.FunctionInfraRural).all()
        if growth_data:
            max_phc_growth = None
            max_phc_growth_pct = 0
            
            for state in growth_data:
                if state.phcs_2005 > 0:
                    growth_pct = ((state.phcs_2023 - state.phcs_2005) / state.phcs_2005) * 100
                    if growth_pct > max_phc_growth_pct:
                        max_phc_growth_pct = growth_pct
                        max_phc_growth = state
            
            if max_phc_growth and max_phc_growth_pct > 0:
                insights.append({
                    'type': 'success',
                    'icon': 'fa-line-chart',
                    'title': 'Highest PHC Growth (2005-2023)',
                    'value': f"+{max_phc_growth_pct:.0f}%",
                    'description': f"{max_phc_growth.state_ut} achieved {max_phc_growth_pct:.0f}% growth in PHCs"
                })
        
        if growth_data:
            max_chc_growth = None
            max_chc_growth_pct = 0
            
            for state in growth_data:
                if state.chcs_2005 > 0:
                    growth_pct = ((state.chcs_2023 - state.chcs_2005) / state.chcs_2005) * 100
                    if growth_pct > max_chc_growth_pct:
                        max_chc_growth_pct = growth_pct
                        max_chc_growth = state
            
            if max_chc_growth and max_chc_growth_pct > 0:
                insights.append({
                    'type': 'success',
                    'icon': 'fa-area-chart',
                    'title': 'Highest CHC Growth (2005-2023)',
                    'value': f"+{max_chc_growth_pct:.0f}%",
                    'description': f"{max_chc_growth.state_ut} achieved {max_chc_growth_pct:.0f}% growth in CHCs"
                })
        
        doctor_data = db.query(models.MOPHCRural).all()
        if doctor_data:
            max_vacancy = None
            max_vacancy_rate = 0
            
            for state in doctor_data:
                if state.sanctioned_2023 > 0:
                    vacancy_rate = (state.vacant_2023 / state.sanctioned_2023) * 100
                    if vacancy_rate > max_vacancy_rate:
                        max_vacancy_rate = vacancy_rate
                        max_vacancy = state
            
            if max_vacancy and max_vacancy_rate > 0:
                insights.append({
                    'type': 'warning',
                    'icon': 'fa-user-md',
                    'title': 'Highest Doctor Vacancy Rate',
                    'value': f"{max_vacancy_rate:.0f}%",
                    'description': f"{max_vacancy.state_ut} has {max_vacancy_rate:.0f}% doctor vacancies in PHCs"
                })
        
        total_specialist_shortfall = db.query(
            func.sum(models.SpecialistCHCRural.shortfall_2023)
        ).scalar()
        if total_specialist_shortfall and total_specialist_shortfall > 0:
            insights.append({
                'type': 'critical',
                'icon': 'fa-stethoscope',
                'title': 'National Specialist Shortfall',
                'value': f"{int(total_specialist_shortfall):,}",
                'description': f"India faces a shortfall of {int(total_specialist_shortfall):,} specialists at CHCs"
            })
        
        return insights
    finally:
        db.close()


def get_overview_ranking():
    db = get_db()
    rankings = {}
    
    try:
        imr_best = db.query(models.IMR).order_by(
            models.IMR.imr_total.asc()
        ).limit(5).all()
        rankings['imr_best'] = [
            {'State/UT': state.state_ut, 'IMR Total': state.imr_total}
            for state in imr_best
        ]

        imr_worst = db.query(models.IMR).order_by(
            models.IMR.imr_total.desc()
        ).limit(5).all()
        rankings['imr_worst'] = [
            {'State/UT': state.state_ut, 'IMR Total': state.imr_total}
            for state in imr_worst
        ]

        phc_shortfall = db.query(models.Shortfall).filter(
            models.Shortfall.phc_shortfall_pct > 0
        ).order_by(models.Shortfall.phc_shortfall_pct.desc()).limit(5).all()
        rankings['phc_shortfall_worst'] = [
            {'State/UT': state.state_ut, 'PHCs % Shortfall': state.phc_shortfall_pct}
            for state in phc_shortfall
        ]
        return rankings
    finally:
        db.close()


def get_shortfall():
    db = get_db()
    try:
        shortfall_data = db.query(models.Shortfall).all()
        if not shortfall_data:
            return {}
        return {
            'labels': [state.state_ut for state in shortfall_data],
            'sc_shortfall': [state.sc_shortfall_pct for state in shortfall_data],
            'phc_shortfall': [state.phc_shortfall_pct for state in shortfall_data],
            'chc_shortfall': [state.chc_shortfall_pct for state in shortfall_data],
            'sc_required': [state.sc_required for state in shortfall_data],
            'sc_present': [state.sc_present for state in shortfall_data],
            'phc_required': [state.phc_required for state in shortfall_data],
            'phc_present': [state.phc_present for state in shortfall_data],
            'chc_required': [state.chc_required for state in shortfall_data],
            'chc_present': [state.chc_present for state in shortfall_data],
        }
    finally:
        db.close()