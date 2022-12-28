from unittest.mock import MagicMock
from unittest.mock import patch

from app.database import Job
from app.database import Student


@patch('app.blueprint.routes.filter_student_record_by_avg')
@patch('app.blueprint.routes.update_student_record')
def test_advice_job(
        mock_update_student_record: MagicMock,
        mock_filter_student_record_by_avg: MagicMock,
        client,
):
    input_grades = {
        'math': 1,
        'physics': 1,
        'chemistry': 1,
        'biology': 10,
        'literature': 10,
        'history': 10,
        'philosophy': 10,
        'art': 10,
        'foreign_lang': 10,
    }

    student1 = Student(
        student_id='mock_id1',
        math=1,
        physics=2,
        chemistry=1,
        biology=9,
        literature=10,
        history=10,
        philosophy=10,
        art=10,
        foreign_lang=10,
    )
    student1.jobs = [
        Job(job_name='job1', salary=50), Job(job_name='job2', salary=50),
        Job(job_name='job3', salary=50), Job(job_name='job4', salary=50),
        Job(job_name='job5', salary=50), Job(job_name='job4', salary=50),
    ]

    student2 = Student(
        student_id='mock_id2',
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
    student2.jobs = [
        Job(job_name='job11', salary=50), Job(job_name='job12', salary=50),
        Job(job_name='job13', salary=50), Job(job_name='job14', salary=50),
        Job(job_name='job15', salary=50), Job(job_name='job14', salary=50),
    ]

    mock_filter_student_record_by_avg.return_value = [
        student1,
        student2,
    ]

    result = client.post(
        '/1/advices', json=input_grades,
        headers={'Content-Type': 'application/json'},
    )
    mock_update_student_record.assert_called_with('1', input_grades)
    mock_filter_student_record_by_avg.assert_called_with(7.0)
    assert result.json == {
        'message': [
            'job4', 'job1', 'job2',
        ], 'status': 'success',
    }


@patch('app.blueprint.routes.filter_student_record_by_avg')
@patch('app.blueprint.routes.update_student_record')
def test_not_found_advice_job(
        mock_update_student_record: MagicMock,
        mock_filter_student_record_by_avg: MagicMock,
        client,
):
    input_grades = {
        'math': 1,
        'physics': 1,
        'chemistry': 1,
        'biology': 10,
        'literature': 10,
        'history': 10,
        'philosophy': 10,
        'art': 10,
        'foreign_lang': 10,
    }

    student1 = Student(
        student_id='mock_id2',
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
    student1.jobs = [
        Job(job_name='job11', salary=50), Job(job_name='job12', salary=50),
        Job(job_name='job13', salary=50), Job(job_name='job14', salary=50),
        Job(job_name='job15', salary=50), Job(job_name='job14', salary=50),
    ]

    mock_filter_student_record_by_avg.return_value = [
        student1,
    ]

    result = client.post(
        '/100/advices', json=input_grades,
        headers={'Content-Type': 'application/json'},
    )
    mock_update_student_record.assert_called_with('100', input_grades)
    mock_filter_student_record_by_avg.assert_called_with(7.0)
    assert result.json == {
        'message': [
            'whatever you love!',
        ], 'status': 'success',
    }
