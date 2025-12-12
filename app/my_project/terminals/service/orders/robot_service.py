# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import Robot
from my_project.terminals.service.__init__ import RobotDAO
from my_project.database import db


class RobotService(GeneralService):

    def __init__(self):
        super().__init__(RobotDAO(), Robot)


    def get_all(self):
        return db.session.query(self.Robot).all()  # Get all robots


