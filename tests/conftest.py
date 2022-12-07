import pytest
from pathlib import Path

@pytest.fixture(autouse=True)
def create_a_file():
    path = Path.home()
    with open(path/"killme.txt", "w") as f:
        f.write("test file to be deleted")
    assert len(list(path.glob("*killme*"))) == 1