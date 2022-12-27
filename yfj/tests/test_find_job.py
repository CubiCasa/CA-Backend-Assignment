from unittest import mock

import pytest
from app import create_app
from app.blueprint.routes import find_job


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
        'ENCRYPT_KEY': 'nYRiebe_90xmDXHA16424JOgb9om9sbp9OV7Z-1ONl1=',
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


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
