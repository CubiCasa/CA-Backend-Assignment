import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })
    # other setup can go here
    yield app


@pytest.fixture
def client(app):
    return app.test_client()

# @pytest.mark.parametrize(
#     'request_input, status_expected', [
#         [
#             '/', 'success'
#         ],
#         [
#             '/', 'error'
#         ]
#     ]
# )
# def test_job_request(request_input, status_expected):
#     pass
#


def test_success_job_request(
        client,
):
    # with patch('app.blueprint.jobs.load_student_record') as mock_db:
    #     mock_student = Student(
    #         student_id='123',
    #         math=10,
    #         physics=9,
    #         chemistry=8,
    #         biology=7,
    #         literature=6,
    #         history=5,
    #         philosophy=4,
    #         art=3,
    #         foreign_lang=2
    #     )
    #     mock_db.return_value = mock_student
    #

    #     response = client.post("/1/jobs", data=input_jobs)
    #     print(response.data)
    #     mock_db.assert_called_once()
    #     mock_db.assert_called_with(1)
    input_jobs = {
        'jobs': [
            {
                'name': 'doctor',
            },
            {
                'name': 'engineer',
            },
            {
                'name': 'singer',
            },
        ],
    }
    response = client.post('/1/jobs', data=input_jobs)
    print(response.request.data)
