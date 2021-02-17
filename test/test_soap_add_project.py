from model.project import Project
import random
import string

def test_soap_add_project(app, db):
    project = Project(name=random_string("name", 10),
                      description="description", status="development", view_state="private")
    app.session.login(username="administrator", password="root")
    username = "administrator"
    password = "root"
    old_project = app.soap.get_list_projects(username, password)
    app.project.create_new_project(project)
    old_project.append(project)
    new_project = app.soap.get_list_projects(username, password)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])