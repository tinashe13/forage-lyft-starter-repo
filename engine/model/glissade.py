from datetime import datetime, timedelta
from engine.willoughby_engine import WilloughbyEngine

class Glissade(WilloughbyEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date + timedelta(days=365 * 2)  # Use timedelta for date arithmetic
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
