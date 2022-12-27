from unittest import mock
from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from app import create_app
from app.database import Student
from pydantic_models.jobs import JobPydantic


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@patch('app.blueprint.routes.update_job_record')
@patch('app.blueprint.routes.load_student_record')
def test_advice_job_request(
        mock_load_student_record: MagicMock,
        mock_update_job_record: MagicMock,
        client,
):
    mock_load_student_record.return_value = Student(
        student_id='mockid',
        math=10,
        physics=10,
        chemistry=10,
        biology=10,
        literature=10,
        history=10,
        philosophy=10,
        art=10,
        foreign_lang=10,
    )
    input_jobs = {
        'jobs': [
            {'name': 'IT technical support officer'}, {
                'name': 'engineer',
            }, {'name': 'singer'},
        ],
    }
    client.post(
        '/1/jobs', json=input_jobs,
        headers={'Content-Type': 'application/json'},
    )
    mock_load_student_record.assert_called_with('1')
    mock_update_job_record.assert_has_calls([
        call('1', JobPydantic(name='IT technical support officer', salary=72000)),
        call('1', JobPydantic(name='engineer', salary=50000)),
        call('1', JobPydantic(name='singer', salary=50000)),

    ])


def test_delete_grade(
        client,
):
    with mock.patch('app.blueprint.routes.delete_student_record') as mock_db:
        client.post(
            '/1/delete_grades',
            headers={'Content-Type': 'application/json'},
        )
        mock_db.assert_called_once()
        mock_db.assert_called_with('1')
