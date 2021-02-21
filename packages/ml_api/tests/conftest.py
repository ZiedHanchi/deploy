import sys
import os
from os.path import dirname, realpath, sep, pardir
from pathlib import Path

if dirname(realpath(__file__)) not in sys.path :
    sys.path.append(dirname(realpath(__file__)))
if dirname(os.getcwd()) not in sys.path :
    sys.path.append(os.getcwd())
if sep.join(dirname(realpath(__file__)).split("/")[:-1]) + sep + "api" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-1]) + sep + "api")
if Path(os.path.dirname(os.path.realpath(__file__))).parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent)) 
if Path(os.path.dirname(os.path.realpath(__file__))).parent.parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent.parent))   

import pytest

from api.app import create_app
from api.config import TestingConfig


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
