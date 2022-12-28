from unittest import mock


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
