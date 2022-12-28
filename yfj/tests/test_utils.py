import json
from unittest import mock
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from app.blueprint.routes import find_job
from app.utils import get_job_market_data


@pytest.mark.parametrize(
    'job_name, expected_salary', [
        ['unknown job', 50000],
        ['IT technical support officer', 72000],
    ],
)
def test_find_job(
        client,
        job_name, expected_salary,
):
    with mock.patch('app.utils.get_job_market_data') as mock_market:
        mock_market.return_value = [['IT technical support officer', 72000]]
        response = find_job(job_name)
        assert response.salary == expected_salary


@patch('app.utils.requests.get')
def test_get_job_market(
    mock_get,
    client,
):
    expected_data = [
        ['singer', 100000],
        ['doctor', 80000],
    ]
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.content = json.dumps(expected_data)
    mock_get.return_value = mock_response
    result = get_job_market_data()

    assert result == expected_data
