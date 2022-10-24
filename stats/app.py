import json
import os
import random
from datetime import date

from faker import Faker

from flask import Flask, send_file

fake = Faker()
app = Flask(__name__)


@app.route("/job_earnings")
def get_job_earnings():
    year = date.today().year
    filename = f"job_stats_{year}.json"

    if not os.path.isfile(filename):
        jobs = {}
        for _ in range(1000):
            job = fake.job()
            earning = random.randint(30, 100) * 1000
            jobs[job] = earning

        with open(filename, 'w') as f:
            json.dump(list(jobs.items()), f)

    return send_file(filename, as_attachment=False)


if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app.run(host='0.0.0.0', port=port)
