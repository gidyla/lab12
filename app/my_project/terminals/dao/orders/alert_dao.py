from my_project.terminals.dao.general_dao import GeneralDAO

class AlertDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Alert
    def __init__(self):
        super().__init__(self.Alert)