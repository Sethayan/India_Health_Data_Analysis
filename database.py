from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

Base = declarative_base()

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'appDatabase.db')
DATABASE_URL = f'sqlite:///{DATABASE_PATH}'

_engine = None
_session_factory = None

class StateWiseSCPHCCHCCount(Base):
    __tablename__ = 'sc_phc_chc_count'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    sub_centres_rural = Column(Integer)
    sub_centres_urban = Column(Integer)
    phcs_rural = Column(Integer)
    phcs_urban = Column(Integer)
    chcs_rural = Column(Integer)
    chcs_urban = Column(Integer)


class StateWiseSDHDHMCCount(Base):
    __tablename__ = 'sdh_dh_mc_count'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    sub_divisional_hospital = Column(Integer)
    district_hospital = Column(Integer)
    medical_colleges = Column(Integer)


class FunctionInfraRural(Base):
    __tablename__ = 'function_infra_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    sub_centre_2005 = Column(Integer)
    phcs_2005 = Column(Integer)
    chcs_2005 = Column(Integer)
    sub_centre_2023 = Column(Integer)
    phcs_2023 = Column(Integer)
    chcs_2023 = Column(Integer)


class BuildingSCRural(Base):
    __tablename__ = 'building_sc_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    total_sub_centers_2005 = Column(Integer)
    govt_building_2005 = Column(Integer)
    rented_building_2005 = Column(Integer)
    rent_free_building_2005 = Column(Integer)
    total_sub_centers_2023 = Column(Integer)
    govt_building_2023 = Column(Integer)
    rented_building_2023 = Column(Integer)
    rent_free_building_2023 = Column(Integer)


class BuildingPHCRural(Base):
    __tablename__ = 'building_phc_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    total_phcs_2005 = Column(Integer)
    govt_building_2005 = Column(Integer)
    rented_building_2005 = Column(Integer)
    rent_free_building_2005 = Column(Integer)
    total_phcs_2023 = Column(Integer)
    govt_building_2023 = Column(Integer)
    rented_building_2023 = Column(Integer)
    rent_free_building_2023 = Column(Integer)


class BuildingCHCRural(Base):
    __tablename__ = 'building_chc_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    total_chcs_2005 = Column(Integer)
    govt_building_2005 = Column(Integer)
    rented_building_2005 = Column(Integer)
    rent_free_building_2005 = Column(Integer)
    total_chcs_2023 = Column(Integer)
    govt_building_2023 = Column(Integer)
    rented_building_2023 = Column(Integer)
    rent_free_building_2023 = Column(Integer)


class MOPHCRural(Base):
    __tablename__ = 'mo_phc_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    required_2005 = Column(Integer)
    sanctioned_2005 = Column(Integer)
    in_position_2005 = Column(Integer)
    vacant_2005 = Column(Integer)
    shortfall_2005 = Column(Integer)
    required_2023 = Column(Integer)
    sanctioned_2023 = Column(Integer)
    in_position_2023 = Column(Integer)
    vacant_2023 = Column(Integer)
    shortfall_2023 = Column(Integer)


class SpecialistCHCRural(Base):
    __tablename__ = 'specialist_chc_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    required_2005 = Column(Integer)
    sanctioned_2005 = Column(Integer)
    in_position_2005 = Column(Integer)
    vacant_2005 = Column(Integer)
    shortfall_2005 = Column(Integer)
    required_2023 = Column(Integer)
    sanctioned_2023 = Column(Integer)
    in_position_2023 = Column(Integer)
    vacant_2023 = Column(Integer)
    shortfall_2023 = Column(Integer)


class RadiograpjersCHCRural(Base):
    __tablename__ = 'radiographers_chc_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    required_2005 = Column(Integer)
    sanctioned_2005 = Column(Integer)
    in_position_2005 = Column(Integer)
    vacant_2005 = Column(Integer)
    shortfall_2005 = Column(Integer)
    required_2023 = Column(Integer)
    sanctioned_2023 = Column(Integer)
    in_position_2023 = Column(Integer)
    vacant_2023 = Column(Integer)
    shortfall_2023 = Column(Integer)


class PharmacistRural(Base):
    __tablename__ = 'pharmacist_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    required_2005 = Column(Integer)
    sanctioned_2005 = Column(Integer)
    in_position_2005 = Column(Integer)
    vacant_2005 = Column(Integer)
    shortfall_2005 = Column(Integer)
    required_2023 = Column(Integer)
    sanctioned_2023 = Column(Integer)
    in_position_2023 = Column(Integer)
    vacant_2023 = Column(Integer)
    shortfall_2023 = Column(Integer)


class LabTechRural(Base):
    __tablename__ = 'lab_tech_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    required_2005 = Column(Integer)
    sanctioned_2005 = Column(Integer)
    in_position_2005 = Column(Integer)
    vacant_2005 = Column(Integer)
    shortfall_2005 = Column(Integer)
    required_2023 = Column(Integer)
    sanctioned_2023 = Column(Integer)
    in_position_2023 = Column(Integer)
    vacant_2023 = Column(Integer)
    shortfall_2023 = Column(Integer)


class NursingRural(Base):
    __tablename__ = 'nursing_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    required_2005 = Column(Integer)
    sanctioned_2005 = Column(Integer)
    in_position_2005 = Column(Integer)
    vacant_2005 = Column(Integer)
    shortfall_2005 = Column(Integer)
    required_2023 = Column(Integer)
    sanctioned_2023 = Column(Integer)
    in_position_2023 = Column(Integer)
    vacant_2023 = Column(Integer)
    shortfall_2023 = Column(Integer)


class FunctionSCPHCCHCRural(Base):
    __tablename__ = 'function_sc_phc_chc_rural'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    sub_centre_march_2022 = Column(Integer)
    phcs_march_2022 = Column(Integer)
    chcs_march_2022 = Column(Integer)
    sub_centre_march_2023 = Column(Integer)
    phcs_march_2023 = Column(Integer)
    chcs_march_2023 = Column(Integer)


class BuildingPosition20222023(Base):
    __tablename__ = 'building_position_2022_2023'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    sc_total_march_2022 = Column(Integer)
    sc_govt_march_2022 = Column(Integer)
    sc_total_march_2023 = Column(Integer)
    sc_govt_march_2023 = Column(Integer)
    phc_total_march_2022 = Column(Integer)
    phc_govt_march_2022 = Column(Integer)
    phc_total_march_2023 = Column(Integer)
    phc_govt_march_2023 = Column(Integer)
    chc_total_march_2022 = Column(Integer)
    chc_govt_march_2022 = Column(Integer)
    chc_total_march_2023 = Column(Integer)
    chc_govt_march_2023 = Column(Integer)


class ManpowerPart1(Base):
    __tablename__ = 'manpower_part1'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    doctors_phc_march_2022 = Column(Integer)
    doctors_phc_march_2023 = Column(Integer)
    specialists_chc_march_2022 = Column(Integer)
    specialists_chc_march_2023 = Column(Integer)


class ManpowerPart2(Base):
    __tablename__ = 'manpower_part2'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    radiographers_march_2022 = Column(Integer)
    radiographers_march_2023 = Column(Integer)
    pharmacists_march_2022 = Column(Integer)
    pharmacists_march_2023 = Column(Integer)
    lab_tech_march_2022 = Column(Integer)
    lab_tech_march_2023 = Column(Integer)
    nursing_march_2022 = Column(Integer)
    nursing_march_2023 = Column(Integer)


class DistrictWiseInfra(Base):
    __tablename__ = 'district_wise_infra'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    district_name = Column(String(100))
    sub_centres_rural = Column(Integer)
    sub_centres_urban = Column(Integer)
    phcs_rural = Column(Integer)
    phcs_urban = Column(Integer)
    chcs_rural = Column(Integer)
    chcs_urban = Column(Integer)
    sub_divisional_hospital = Column(Integer)
    district_hospital = Column(Integer)
    medical_college = Column(Integer)


class StateArea(Base):
    __tablename__ = 'state_area'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    tribal_area_sq_km = Column(Float)
    rural_area_sq_km = Column(Float)
    urban_area_sq_km = Column(Float)
    total_area_sq_km = Column(Float)
    rural_percentage = Column(Float)
    number_of_districts = Column(Integer)
    number_of_villages = Column(Integer)


class StatePopulation(Base):
    __tablename__ = 'state_population'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    pop_2011_rural = Column(Integer)
    pop_2011_urban = Column(Integer)
    pop_2011_total = Column(Integer)
    pop_2011_rural_pct = Column(Float)
    pop_2023_rural = Column(Integer)
    pop_2023_urban = Column(Integer)
    pop_2023_total = Column(Integer)
    pop_2023_rural_pct = Column(Float)


class StateDensity(Base):
    __tablename__ = 'state_density'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    density_rural = Column(Integer)
    density_urban = Column(Integer)
    density_total = Column(Integer)


class BirthDeathRate(Base):
    __tablename__ = 'birth_death_rate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    birth_rate_total = Column(Float)
    birth_rate_rural = Column(Float)
    birth_rate_urban = Column(Float)
    death_rate_total = Column(Float)
    death_rate_rural = Column(Float)
    death_rate_urban = Column(Float)


class IMR(Base):
    __tablename__ = 'imr'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    imr_total = Column(Integer)
    imr_rural = Column(Integer)
    imr_urban = Column(Integer)


class Shortfall(Base):
    __tablename__ = 'shortfall'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    pop_rural = Column(Integer)
    pop_tribal = Column(Integer)
    sc_required = Column(Integer)
    sc_present = Column(Integer)
    sc_shortfall = Column(Integer)
    sc_shortfall_pct = Column(Float)
    phc_required = Column(Integer)
    phc_present = Column(Integer)
    phc_shortfall = Column(Integer)
    phc_shortfall_pct = Column(Float)
    chc_required = Column(Integer)
    chc_present = Column(Integer)
    chc_shortfall = Column(Integer)
    chc_shortfall_pct = Column(Float)


class BuildingSCPosition(Base):
    __tablename__ = 'building_sc_position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    total_sub_centers = Column(Integer)
    govt_buildings = Column(Integer)
    rented_buildings = Column(Integer)
    rent_free_buildings = Column(Integer)
    buildings_required = Column(Integer)


class BuildingPHCPosition(Base):
    __tablename__ = 'building_phc_position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    total_phcs = Column(Integer)
    govt_buildings = Column(Integer)
    rented_buildings = Column(Integer)
    rent_free_buildings = Column(Integer)
    buildings_required = Column(Integer)


class BuildingCHCPosition(Base):
    __tablename__ = 'building_chc_position'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_ut = Column(String(100))
    total_chcs = Column(Integer)
    govt_buildings = Column(Integer)
    rented_buildings = Column(Integer)
    rent_free_buildings = Column(Integer)
    buildings_required = Column(Integer)

def init_engine():
    global _engine
    if _engine is None:
        url = DATABASE_URL
        _engine = create_engine(
            url,
            pool_pre_ping=True
        )
    return _engine


def init_session_factory():
    global _session_factory
    if _session_factory is None:
        engine = init_engine()
        _session_factory = scoped_session(sessionmaker(bind=engine))
    return _session_factory


def get_db():
    session_factory = init_session_factory()
    return session_factory()

class models:
    StateWiseSCPHCCHCCount = StateWiseSCPHCCHCCount
    StateWiseSDHDHMCCount = StateWiseSDHDHMCCount
    FunctionInfraRural = FunctionInfraRural
    BuildingSCRural = BuildingSCRural
    BuildingPHCRural = BuildingPHCRural
    BuildingCHCRural = BuildingCHCRural
    MOPHCRural = MOPHCRural
    SpecialistCHCRural = SpecialistCHCRural
    RadiograpjersCHCRural = RadiograpjersCHCRural
    PharmacistRural = PharmacistRural
    LabTechRural = LabTechRural
    NursingRural = NursingRural
    FunctionSCPHCCHCRural = FunctionSCPHCCHCRural
    BuildingPosition20222023 = BuildingPosition20222023
    ManpowerPart1 = ManpowerPart1
    ManpowerPart2 = ManpowerPart2
    DistrictWiseInfra = DistrictWiseInfra
    StateArea = StateArea
    StatePopulation = StatePopulation
    StateDensity = StateDensity
    BirthDeathRate = BirthDeathRate
    IMR = IMR
    Shortfall = Shortfall
    BuildingSCPosition = BuildingSCPosition
    BuildingPHCPosition = BuildingPHCPosition
    BuildingCHCPosition = BuildingCHCPosition