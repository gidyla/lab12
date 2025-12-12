from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import UserService
from my_project.terminals.controller.utils import handle_error, handle_response

class UserController(GeneralController):
    def __init__(self):
        super().__init__(UserService())

    def get_user_robot_controls(self, user_id):
        user = self.service.dao.get_by_id(user_id)
        if user:
            return handle_response(user.to_dict(), 200)
        else:
            return handle_error("User not found", 404)
