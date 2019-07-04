from flask import Flask
from flask_restful import Api
from cloghandler import ConcurrentRotatingFileHandler
import logging.handlers
from app.utils.configs import ConfigsParser
from app.views.index import Index

configs = ConfigsParser.parse_configs('app')

log_file = configs.get('log_file')
log_file_size = 1024 * 1024 * 1024 * 10
handler = ConcurrentRotatingFileHandler(log_file, "a", log_file_size, 1000)
formatter = logging.Formatter(
    '%(asctime)s] - %(name)s - %(levelname)s in %(module)s:%(lineno)d:%(funcName)-10s %(message)s')
handler.setFormatter(formatter)

app = Flask(__name__)
app.logger.addHandler(handler)
app.logger.setLevel(logging.DEBUG)
api = Api(app)

api.add_resource(Index, "/")


if __name__ == "__main__":
    app.run(debug=True, port=9001, host='0.0.0.0')
