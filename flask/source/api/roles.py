from ..db import db , model
from .. import config
from flask import jsonify   

rowtodict = lambda row: dict((col, getattr(row, col)) for col in row.__table__.columns.keys())
dictObj = {}

def getTeamRoles(logger, team):
    engine = db.getDBConnection(config.database)
    session = db.getSession(engine)
    rolesList = [rowtodict(row) for row in session.query(model.Roles).filter(model.Roles.team == team).all()]
    teamRoles = [role['role'] for role in rolesList]
    return teamRoles

def insertRole(logger, team, role):
    engine = db.getDBConnection(config.database)
    from datetime import datetime
    objectInstance = model.Roles(team=team,role=role,created_at = datetime.now())
    db.insertData(engine, objectInstance)

# def insertRoles(rolesArray):
#     from sqlalchemy.dialects.postgresql import insert
#     stmt=insert('roles',rolesArray)
#     engine = db.getDBConnection(config.database)

