import copy
import sys
from pathlib import Path

from fastapi.testclient import TestClient
import pytest

# Ensure tests can import the app module from src/
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "src"))

import app as app_module

_app = app_module.app
_activities_backup = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_activities_backup))
    yield


@pytest.fixture
def client():
    return TestClient(_app)
