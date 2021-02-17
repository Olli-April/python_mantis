from model.project import Project
import random
import string

def test_add_project(app, db):
    app.session.login(username="administrator", password= "root")
    project = Project(name=random_string("name", 10), description="description", status="development",
                      view_state="private")
    old_project_list = db.get_project_list()
    app.project.create_new_project(project)
    app.session.logout()
    new_project_list = db.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])