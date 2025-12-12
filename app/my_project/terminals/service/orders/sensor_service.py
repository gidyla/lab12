# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import Sensor
from my_project.terminals.service.__init__ import SensorDAO


class SensorService(GeneralService):

    def __init__(self):
        super().__init__(SensorDAO(), Sensor)
