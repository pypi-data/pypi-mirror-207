from pms import user_controller
import pathlib
from pms import db_functions

username = "ahmad"
password = "123"


def pre_set_db(module=user_controller, db_manager=db_functions):
    path = pathlib.Path.joinpath(pathlib.Path(__file__).parent, "sql_testing.db")
    module.db_path = path
    try:
        db_manager.delete_db(path)
    except FileNotFoundError:
        pass


def test_user_signup():
    pre_set_db()
    user = user_controller.signup_user("ahmad", "123")
    assert user is not None


def test_user_signup_already_in():
    pre_set_db()
    user1 = user_controller.signup_user(username, password)
    assert user1 is not None
    user2 = user_controller.signup_user(username, password)
    assert user2 is None


def test_login_valid_user(capsys):
    pre_set_db()
    user_controller.signup_user(username, password)
    user_controller.login_user(username, password)
    captured = capsys.readouterr()
    assert "user logged in" in captured.out


def test_login_user_invalid_username():
    pre_set_db()
    user_controller.signup_user(username, password)
    user = user_controller.login_user(username + "1", password)
    assert user is None


def test_login_user_invalid_password():
    pre_set_db()
    user_controller.signup_user(username, password)
    try:
        user = user_controller.login_user(username, password + "1")
        assert user is None
    except Exception as e:
        print(e)
        assert False


def test_double_login():
    pre_set_db()
    user_controller.signup_user(username, password)
    user_controller.signup_user(username + "1", password)
    user_controller.login_user(username, password)
    user = user_controller.login_user(username + "1", password)
    assert user is None


def test_logout(capsys):
    pre_set_db()
    user_controller.signup_user(username, password)
    user_controller.login_user(username, password)
    user_controller.logout()
    captured = capsys.readouterr()
    assert "user logged out" in captured.out


def test_logout_without_login(capsys):
    pre_set_db()
    user_controller.signup_user(username, password)
    user_controller.logout()
    captured = capsys.readouterr()
    assert "user not login!" in captured.out


def test_logout_twice(capsys):
    pre_set_db()
    user_controller.signup_user(username, password)
    user_controller.logout()
    user_controller.logout()
    captured = capsys.readouterr()
    assert "user not login!" in captured.out
