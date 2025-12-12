from my_project.terminals.dao.general_dao import GeneralDAO

class ZoneDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Zone
    def __init__(self):
        super().__init__(self.Zone)