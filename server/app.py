from flask import Flask, make_response, jsonify,request
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
Migrate(app, db)

CORS(app)

@app.route('/movies', methods=['GET'])
def movies():
    if request.method == ['GET']:
         movies = Movie.query.all()

         return make_response(
              jsonify([movie.to_dict() for movie in movies]),200,
         )
    return make_response(
         jsonify({'text':'Method Not Allowed'},405,))

if __name__=='__main__':
      app.run(port=5555)