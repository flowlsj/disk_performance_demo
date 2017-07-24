from app import flask_app
from api import performance

if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", debug=1)
