from os import getenv

from flask import Flask, redirect, url_for
from flask_migrate import Migrate

from views.posts import diary_app
from models import db

app = Flask(__name__)
app.register_blueprint(diary_app)


@app.route('/')
def index():
    return redirect(url_for('diary_app.list'), code=302)


CONFIG_NAME = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
