import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    branch_name = request.args.get("branch_name")
    if branch_name:
        return jsonified(branch_name)
    else:
        return [{}]

def jsonified(branch_name: str) -> list:
    statement = f"SELECT * FROM banks JOIN branches ON banks.id=branches.bank_id WHERE branch={branch_name} LIMIT 10;"
    results = db.engine.execute(toSingle(statement))
    jsonified = json.dumps([dict(result) for result in results])
    return jsonified

def toSingle(statement:str) -> str:
    return statement.replace('"', "'")


if __name__ == 'main':
    app.run()