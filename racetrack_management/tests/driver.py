from src.services.racetrack_management_service import IRaceTrackManagementService
from src.services.impl.racetrack_management_service import RaceTrackManagementService

rms: IRaceTrackManagementService = RaceTrackManagementService()
rms.create_booking("CAR", "O34", "15:00")
rms.extend_booking("O34", "22:00")
rms.get_revenue()