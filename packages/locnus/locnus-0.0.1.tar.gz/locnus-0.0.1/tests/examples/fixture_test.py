import pytest


@pytest.fixture(scope="session")
def one():
    return 1


@pytest.fixture(scope="session", autouse=True)
def two():
    print("two was used..")
    return 2


def test_fixtures(one, rf):
    print(one)
    # assert False
    assert True
