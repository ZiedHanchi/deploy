import sys
import os
from os.path import dirname, realpath, sep, pardir

if dirname(realpath(__file__)) not in sys.path :
    sys.path.append(dirname(realpath(__file__)))
if dirname(os.getcwd()) not in sys.path :
    sys.path.append(os.getcwd())
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model")
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model")
if sep.join(dirname(realpath(__file__)).split("/")[:-1]) + sep + "api" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-1]) + sep + "api")

import json

from regression_model.config import config
from regression_model.processing.data_management import load_dataset


def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    # Load the test data from the regression_model package.
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_dataset(file_name=config.TESTING_DATA_FILE)
    post_json = test_data.to_json(orient='records')

    # When
    response = flask_test_client.post('/v1/predict/regression',
                                      json=json.loads(post_json))

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)

    # Check correct number of errors removed
    assert len(response_json.get('predictions')) + len(
        response_json.get('errors')) == len(test_data)
