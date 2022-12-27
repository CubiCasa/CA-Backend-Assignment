from app import create_app


def test_index_route():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'The server is running!'
