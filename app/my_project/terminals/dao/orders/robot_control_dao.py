from my_project.terminals.dao.general_dao import GeneralDAO

class RobotControlDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import RobotControl
    def __init__(self):
        super().__init__(self.RobotControl)

    def get_all_with_user(self):
        from my_project.database import db
        # Fetch all robot control records with related user information
        return db.session.query(self.RobotControl).all()
