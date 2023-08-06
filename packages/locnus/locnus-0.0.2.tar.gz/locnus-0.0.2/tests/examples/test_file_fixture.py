from pathlib import Path

import pytest


@pytest.fixture()
def some_file_path():
    return Path(__file__).parent / "some_file.txt"


@pytest.fixture()
def some_file(some_file_path):
    """
    This fixture creates a file in the same directory as this file.
    It gets removed after the test is run.
    """
    path = Path(__file__).parent / "some_file.txt"
    with path.open("w") as f:
        f.write("Hello, world!")
    yield path
    path.unlink()


def test_some_file(some_file):
    with some_file.open() as f:
        assert f.read() == "Hello, world!"


def test_some_file_again(some_file_path):
    assert not some_file_path.exists()
