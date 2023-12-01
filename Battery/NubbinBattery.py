from abc import ABC
from datetime import datetime, date

from car import Car


class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = date.today()  # Use date.today() to get the current date
        self.last_service_date = datetime.strptime(last_service_date, '%Y-%m-%d').date()

    def battery_should_be_serviced(self):
        return (self.current_date - self.last_service_date).days > 1460
