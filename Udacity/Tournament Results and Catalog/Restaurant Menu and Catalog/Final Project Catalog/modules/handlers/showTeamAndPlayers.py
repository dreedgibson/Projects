from flask import Flask, render_template, flash
from sqlalchemy import asc
from flask import session as login_session
from ..functions.userfunctions import getUserInfo
from ..setup.catalog_setup import Base, Team, Batter, User


def showTeamsHandler(session):
    teams = session.query(Team).order_by(asc(Team.name))
    if 'username' not in login_session:
        return render_template('publicteams.html', teams=teams)
    else:
        return render_template('teams.html', teams=teams)


def showRosterHandler(team_id, session):
    team = session.query(Team).filter_by(id=team_id).one()
    c = getUserInfo(team.user_id, session)
    batters = session.query(Batter).filter_by(team_id=team_id).all()
    if 'username' not in login_session or c.id != login_session['user_id']:
        return render_template('publicroster.html', batters=batters,
                               team=team, creator=c)
    else:
        return render_template('roster.html', batters=batters, team=team,
                               creator=c)
