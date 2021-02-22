import sys
import os
from os.path import dirname, realpath, sep, pardir
from pathlib import Path

if dirname(realpath(__file__)) not in sys.path :
    sys.path.append(dirname(realpath(__file__)))
if dirname(os.getcwd()) not in sys.path :
    sys.path.append(os.getcwd())
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model")
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model")
if Path(os.path.dirname(os.path.realpath(__file__))).parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent))   

import pytest

#from api.app import create_app
#from api.config import TestingConfig
import api.app as ap
import api.config as ac
@pytest.fixture
def app():
    app = ap.create_app(config_object=ac.TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client

