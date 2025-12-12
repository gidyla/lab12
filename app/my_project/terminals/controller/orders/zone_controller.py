from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import ZoneService
from my_project.terminals.controller.utils import handle_error, handle_response

class ZoneController(GeneralController):
    def __init__(self):
        super().__init__(ZoneService())