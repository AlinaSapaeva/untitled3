from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="edit", header="edit", footer="edit"))
    app.session.logout()
