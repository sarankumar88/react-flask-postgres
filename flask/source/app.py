# Standard
from gevent.pywsgi import WSGIServer
from flask import Flask , jsonify , request
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Custom
from .db import db
from .api import roles as roles_api
from . import config , log_config
import logging
 
app = Flask(__name__)

# CORS(app)


logging.basicConfig(filename = 'aap_roles.log', level=logging.DEBUG, format =f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

logger = log_config.getLogger(__name__,config.logFileName)

engine = db.getDBConnection(config.database)
db.initializeDatabase(engine)

@app.route('/api/role' , methods=['POST'])
def addRole():
    try:
        data = request.json
        logger.info(data)
        roles_api.insertRole(logger, data['team'], data['role'])
        return jsonify({"status": "success", "message" :  "data inserted"}) , 200
    except BaseException as be:
        logger.error("addRole:Error inserting role")
        logger.error(be)
        return jsonify({"status": "failed", "message" :  str(be)}) , 400

@app.route('/api/role/<team>' , methods=['GET'])
def getRole(team):
    try:
        roles = roles_api.getTeamRoles(logger, team)
        return jsonify(roles) , 200
    except BaseException as be:
        logger.error("getRole:Error getting roles")
        logger.error(be)
        return jsonify({"status": "failed", "message" :  str(be)}) , 400

if __name__ == "__main__":
    WSGIServer(('0.0.0.0', 5000), app).serve_forever()
    # app.run(host='0.0.0.0',port=5000,threaded=True)