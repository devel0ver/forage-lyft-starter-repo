from datetime import datetime

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_level):
        return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date), CarriganTires(wear_level))

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_level):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date), CarriganTires(wear_level))
    
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on, wear_level):
        return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(last_service_date, current_date), CarriganTires(wear_level))
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_level):
        return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTires(wear_level))
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_level):
        return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date), OctoprimeTires(wear_level))

