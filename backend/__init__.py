# __init__.py（←application.py）

from flask import Flask, render_template
from flask_cors import CORS

app = Flask('FLASK-VUE',
            static_folder = "./dist/static",
            template_folder = "./dist")
app.config.from_object('backend.config.BaseConfig')

from backend.api import api
app.register_blueprint(api, url_prefix="/api")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")