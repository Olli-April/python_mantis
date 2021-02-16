
def test_add_project(app, db, json_project):
    app.session.login("administrator", "root")
    old_project = db.get_project_list()
    app.project.create_new_project(json_project)
    new_project = db.get_project_list()
    assert len(old_project) + 1 == len(new_project) 