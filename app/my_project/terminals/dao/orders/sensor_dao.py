from my_project.terminals.dao.general_dao import GeneralDAO

class SensorDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Sensor
    def __init__(self):
        super().__init__(self.Sensor)