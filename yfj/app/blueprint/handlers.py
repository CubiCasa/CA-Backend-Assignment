"""This module registers the error handler on the application."""
from flask import jsonify
from flask import make_response
from flask.wrappers import Response


def register_handler(app) -> Response:
    """Registers the error handler is a function to common error HTTP codes

    Parameters:
        app (flask.app.Flask): The application instance.
    """

    @app.errorhandler(400)
    def bad_request(error) -> Response:
        """Deal with HTTP BadRequest exceptions.

        Parameters:
            error (BadRequest): A werkzeug.exceptions.BadRequest exception object.

        Returns:
            A flask response object.
        """

        return make_response(
            jsonify({
                'status': 'fail',
                'message': 'bad request',
            }), 400,
        )

    @app.errorhandler(404)
    def not_found(error) -> Response:
        """ Deal with HTTP NotFound exceptions.

        Parameters:
            error (NotFound): A werkzeug.exceptions.NotFound exception object.

        Returns:
            A flask response object.
        """
        return make_response(
            jsonify({
                'status': 'error',
                'message': error.description,
            }), 404,
        )
