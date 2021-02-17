from model.project import Project
import random

def test_delete_project(app, db):
    app.session.login(username="administrator", password="root")
    if len(db.get_project_list()) == 0:
        app.project.create_new_project(Project(name="new", description="description",
                                               status="development", view_state="public"))
    old_project_list = db.get_project_list()
    project_delete = random.choice(old_project_list)
    app.project.delete_project_by_name(project_delete.name)
    new_project_list = db.get_project_list()
    app.session.logout()
    old_project_list.remove(project_delete)
    assert old_project_list == new_project_list
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)