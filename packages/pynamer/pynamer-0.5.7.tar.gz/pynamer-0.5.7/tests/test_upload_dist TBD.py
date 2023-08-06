#!/usr/bin/env python3
# Core Library modules
from pathlib import Path

# Third party modules
import pytest

# First party modules
from pynamer import pynamer

BASE_DIR = Path(__file__).parents[0]


pypirc_text = """[distutils]
index-servers =
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = johndoe
password = amidead"""


@pytest.fixture()
def pre_upload():
    pypirc_file = BASE_DIR / "resources" / "mock_build" / ".pypirc"
    pypirc_file.touch()
    pypirc_file.write_text(pypirc_text)
    yield
    pypirc_file.unlink()
