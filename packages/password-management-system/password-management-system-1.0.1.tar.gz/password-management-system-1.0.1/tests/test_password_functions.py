from tests.test_user_functions import pre_set_db
from pms import user_controller
from pms import password_controller

username = "ahmad"
password = "123"


def signup_and_login_user():
    pre_set_db(user_controller)
    pre_set_db(password_controller)
    user_controller.signup_user(username, password)
    user_controller.login_user(username, password)


def test_add_password(capsys):
    signup_and_login_user()
    password_controller.add_password("1234", "first_p")
    captured = capsys.readouterr()
    assert "password add!" in captured.out


def test_add_password_without_login(capsys):
    pre_set_db()
    user_controller.signup_user(username, password)
    password_controller.add_password("123", "123")
    captured = capsys.readouterr()
    assert "login a user first" in captured.out


def test_show_all_passwords(capsys):
    signup_and_login_user()
    password_controller.add_password("123", "my_pass")
    password_controller.add_password("133", "pass_my")
    password_controller.select_password()
    captured = capsys.readouterr()
    assert f"password:\"{'123'}\"" in captured.out
    assert f"name:{'my_pass'}" in captured.out
    assert f"password:\"{'133'}\"" in captured.out
    assert f"name:{'pass_my'}" in captured.out


def test_show_password_by_name(capsys):
    signup_and_login_user()
    password_controller.add_password("123", "my_pass")
    password_controller.add_password("133", "pass_my")
    password_controller.select_password(name="pass_my")
    captured = capsys.readouterr()
    assert f"password:\"{'123'}\"" not in captured.out
    assert f"name:{'my_pass'}" not in captured.out
    assert f"password:\"{'133'}\"" in captured.out
    assert f"name:{'pass_my'}" in captured.out


def test_show_password_without_add(capsys):
    signup_and_login_user()
    password_controller.select_password()
    captured = capsys.readouterr()
    assert "no passwords matching found!" in captured.out


def test_delete_password(capsys):
    signup_and_login_user()
    password_controller.add_password("123", "my_pass")
    password_controller.select_password()
    captured = capsys.readouterr()
    assert f"password:\"{'123'}\"" in captured.out
    assert f"name:{'my_pass'}" in captured.out
    password_controller.delete_password(password_id="1")
    password_controller.select_password()
    captured = capsys.readouterr()
    assert "no passwords matching found!" in captured.out


def test_delete_same_password_twice(capsys):
    signup_and_login_user()
    password_controller.add_password("123", "my_pass")
    password_controller.delete_password(password_id=1)
    capsys.readouterr()
    password_controller.delete_password(password_id=1)
    captured = capsys.readouterr()
    assert "delete failed: password not found" in captured.out


def test_update_password_valid(capsys):
    signup_and_login_user()
    password_controller.add_password("123", "my_pass")
    password_controller.update_password(password_id="1", new_password="9oo9999")
    captured = capsys.readouterr()
    assert "password updated" in captured.out
    password_controller.select_password(password_id="1")
    captured = capsys.readouterr()
    assert f"password:\"9oo9999\"" in captured.out


def test_update_password_no_argument(capsys):
    signup_and_login_user()
    password_controller.add_password("123", "my_pass")
    password_controller.update_password(password_id="1")
    captured = capsys.readouterr()
    assert "you need to update at least 1 field" in captured.out


def test_update_password_invalid_id(capsys):
    signup_and_login_user()
    password_controller.add_password("123", "my_pass")
    password_controller.update_password(password_id="5")
    captured = capsys.readouterr()
    assert "password id is invalid" in captured.out
