from my_project.terminals.dao.general_dao import GeneralDAO

class RobotDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import Robot
    def __init__(self):
        super().__init__(self.Robot)