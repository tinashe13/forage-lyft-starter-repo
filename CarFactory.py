from datetime import date
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from engine.model.car import Car

class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return Palindrome(current_date, last_service_date, warning_light_on)

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)
