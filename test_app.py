
import pytest
from app import (
    blood_stock,
    add_blood,
    search_blood,
    issue_blood
)


@pytest.fixture(autouse=True)
def reset_stock():
    for group in blood_stock:
        blood_stock[group] = 0


def test_add_blood():
    assert add_blood("A+", 5) is True
    assert search_blood("A+") == 5


def test_search_blood():
    add_blood("B+", 10)
    assert search_blood("B+") == 10


def test_issue_blood():
    add_blood("O+", 10)
    assert issue_blood("O+", 3) is True
    assert search_blood("O+") == 7


def test_insufficient_stock():
    add_blood("AB+", 2)
    assert issue_blood("AB+", 5) is False
    assert search_blood("AB+") == 2


def test_invalid_blood_group():
    assert add_blood("X+", 5) is False
    assert search_blood("X+") is None


def test_invalid_units():
    assert add_blood("A+", 0) is False
    assert issue_blood("A+", -2) is False
