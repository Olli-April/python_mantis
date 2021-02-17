import random
from model.project import Project

def test_soap_del_project(app, db):
    app.session.login(username="administrator", password="root")
    if len(db.get_project_list()) == 0:
        app.project.create_new_project(
            Project(name="project_new", description="description", status="development", view_state="public"))
    username = "administrator"
    password = "root"
    old_project = app.soap.get_list_projects(username, password)
    project = random.choice(old_project)
    app.project.delete_project_by_name(project.name)
    new_project = app.soap.get_list_projects(username, password)
    old_project.remove(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
