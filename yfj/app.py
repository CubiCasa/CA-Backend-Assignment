from flask import Flask
from flask import jsonify
from flask.wrappers import Response
from flask_cors import CORS
from flask_pydantic import validate
from models.advices import Advices
from models.advices import InputJob
from models.grades import Grade

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong() -> Response:
    return jsonify('pong!')


@app.route('/<person_id>/advices', methods=['POST'])
@validate()
def advice_job(person_id: int, body: Grade) -> Response:
    # some computation
    result = Advices(
        advices=[{'name': 'doctor'}, {'name': 'engineer'}, {'name': 'singer'}],
    )
    print(person_id, body)
    return result.json()


@app.route('/<person_id>/jobs', methods=['POST'])
@validate()
def add_jobs(person_id: int, body: InputJob) -> Response:
    # some computation
    result_msg = {'status': 'got u, bro'}
    result_msg['message'] = body.dict()
    return jsonify(result_msg)


if __name__ == '__main__':
    app.run()
