from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch

from pydantic_models.jobs import JobPydantic


@patch('app.blueprint.routes.update_job_record')
@patch('app.utils.get_job_market_data')
@patch('app.blueprint.routes.load_student_record')
def test_add_job(
        mock_load_student_record: MagicMock,
        mock_get_job_market_data: MagicMock,
        mock_update_job_record: MagicMock,
        client,
):
    input_jobs = {
        'jobs': [
            {'name': 'IT technical support officer'}, {
                'name': 'engineer',
            }, {'name': 'singer'},
        ],
    }
    mock_get_job_market_data.return_value = [
        ['IT technical support officer', 72000],
        ['engineer', 50000],
        ['singer', 50000],
    ]
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


@patch('app.blueprint.routes.load_student_record')
def test_add_job_unknown_student(
        mock_load_student_record: MagicMock,
        client,
):
    input_jobs = {
        'jobs': [
            {'name': 'IT technical support officer'}, {
                'name': 'engineer',
            }, {'name': 'singer'},
        ],
    }
    mock_load_student_record.return_value = None

    res = client.post(
        '/1/jobs', json=input_jobs,
        headers={'Content-Type': 'application/json'},
    )
    assert res.json == {
        'message': "This student haven\'t had grades yet.", 'status': 'error',
    }
