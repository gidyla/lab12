from my_project.terminals.dao.general_dao import GeneralDAO

class UserDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import User
    def __init__(self):
        super().__init__(self.User)