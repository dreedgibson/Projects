from flask import jsonify
from ..setup.catalog_setup import Base, Team, Batter


# JSON APIs to view team and player info
def teamRosterJSONHandler(team_id, session):
    team = session.query(Team).filter_by(id=team_id).one()
    batters = session.query(Batter).filter_by(team_id=team_id).all()
    return jsonify(Players=[b.serialize for b in batters])


def batterJSONHandler(team_id, batter_id, session):
    batter = session.query(Batter).filter_by(id=batter_id).one()
    return jsonify(Batter=batter.serialize)


def teamsJSONHandler(session):
    teams = session.query(Team).all()
    return jsonify(Teams=[t.serialize for t in teams])
