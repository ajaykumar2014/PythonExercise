from flask import Flask, request
from flask import jsonify
from config import app

from com.curd.UniversityRepository import UniversityRepository
from com.curd.model.University import University,universitysSchema,universitySchema

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///university_lite_store.db'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
repo = UniversityRepository()
# ma = Marshmallow(app)
# db = SQLAlchemy(app)


# app.json_encoder = CustomJSONEncoder
# db = SQLAlchemy(app)




@app.route('/', methods=['GET'])
def getall():
    records = repo.getAll()
    return universitysSchema.dump(records)


@app.route('/<string:index>', methods=['GET'])
def get_todo(index):
    record = repo.getById(index)
    return universitySchema.dump(record)


@app.route('/save', methods=['POST'])
def persist():
    print(f'{request.get_json()}')
    payload = request.get_json()
    name, country, Domains, WebPages = payload['name'].strip(), payload['country'].strip(), payload['Domains'].strip(), \
                                       payload['WebPages'].strip()
    if not name:
        return 400
    university = University(name=name, country=country, Domains=Domains, WebPages=WebPages)
    print(f'{university},{type(university)}')
    repo.save(university)
    response = jsonify()
    response.status_code = 201
    return response


if __name__ == '__main__':
    app.run()
