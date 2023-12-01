from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine

class Thovex(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date + timedelta(days=365 * 4)  # Use timedelta for date arithmetic
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
