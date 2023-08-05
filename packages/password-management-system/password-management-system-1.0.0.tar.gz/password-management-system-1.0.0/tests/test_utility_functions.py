import re

import pytest
from pms.utility_functions import evaluate_password, generate_password


def test_generate_single_query(capsys):
    generate_password(5, ["a"])
    assert "aaaaa" in capsys.readouterr().out


def test_generate_single_query2(capsys):
    generate_password(5, ["abc"])
    assert re.search(r"[abc]{5}", capsys.readouterr().out)


def test_generate_multiple_queries(capsys):
    generate_password(10, ["a", "b", "c"])
    captured = capsys.readouterr()
    assert re.search(r"[abc]{10}", captured.out)
    assert re.search(r"a", captured.out)
    assert re.search(r"b", captured.out)
    assert re.search(r"c", captured.out)
    assert not re.search(r"d", captured.out)


def test_generate_too_low_length():
    try:
        generate_password(4, ["a", "b", "c", "d", "e"])
        assert False
    except ValueError:
        assert True
    except Exception:
        assert False


@pytest.mark.parametrize("password, expected_result", [
    ("1aB!1aB!", 5),
    ("&ab1&Ab1", 5),
    ("-ab452GF", 5),
    ("abc!@#123", 4),
    ("1111111111", 2),
    ("11111", 1),
    ("aB!", 0)
])
def test_evaluate_passwords(password, expected_result, capsys):
    evaluate_password(password)
    assert str(expected_result) in capsys.readouterr().out

