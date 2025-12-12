from my_project.terminals.dao.general_dao import GeneralDAO

class MaintenanceDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Maintenance
    def __init__(self):
        super().__init__(self.Maintenance)