from my_project.terminals.dao.general_dao import GeneralDAO

class BatteryStatusDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import BatteryStatus
    def __init__(self):
        super().__init__(self.BatteryStatus)