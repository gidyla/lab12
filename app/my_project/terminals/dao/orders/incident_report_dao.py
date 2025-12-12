from my_project.terminals.dao.general_dao import GeneralDAO

class IncidentReportDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import IncidentReport
    def __init__(self):
        super().__init__(self.IncidentReport)