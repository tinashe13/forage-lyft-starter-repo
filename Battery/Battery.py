from abc import ABC, abstractmethod
from datetime import datetime, date

from car import Car

class CarBattery(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d').date()

    @abstractmethod
    def battery_should_be_serviced(self):
        pass