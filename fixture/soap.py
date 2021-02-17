from model.project import Project
from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_projects(self, username, password):
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        list = client.service.mc_projects_get_user_accessible(username, password)
        project_list = []
        for row in list:
            id = row[0]
            name = row[1]
            description = row[7]
            project_list.append(Project(id=str(id), name=name, description=description))
        return project_list