from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.setup.catalog_setup import Base, Team, Batter, User
from modules.functions.userfunctions import getUserID, getUserInfo, createUser
from modules.handlers.showTeamAndPlayers import (showTeamsHandler,
                                                 showRosterHandler)
from modules.handlers.loginLogoutHandlers import (gconnectHandler,
                                                  gdisconnectHandler,
                                                  disconnectHandler,
                                                  showLoginHandler,
                                                  fbconnectHandler,
                                                  fbdisconnectHandler)
from modules.handlers.JSONHandlers import (teamRosterJSONHandler,
                                           batterJSONHandler,
                                           teamsJSONHandler)
from modules.handlers.editDelTeamPlayer import (editTeamHandler,
                                                deleteTeamHandler,
                                                editBatterHandler,
                                                deleteBatterHandler,
                                                newTeamHandler,
                                                newPlayerHandler)

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///teams.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# show the login page
@app.route('/login/')
def showLogin():
    return showLoginHandler()


# google oauth handlers
@app.route('/login/gconnect', methods=['POST'])
def gconnect():
    return gconnectHandler(session)


@app.route('/gdisconnect')
def gdisconnect():
    return gdisconnectHandler()


# facebook login
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    return fbconnectHandler(session)


@app.route('/fbdisconnect')
def fbdisconnect():
    return fbdisconnectHandler()


# global disconnect function
@app.route('/disconnect')
def disconnect():
    return disconnectHandler()


# JSON APIs to view team and player info
@app.route('/teams/<int:team_id>/roster/JSON')
def teamRosterJSON(team_id):
    return teamRosterJSONHandler(team_id, session)


@app.route('/teams/<int:team_id>/roster/<int:batter_id>/JSON')
def batterJSON(team_id, batter_id):
    return batterJSONHandler(team_id, batter_id, session)


@app.route('/teams/JSON')
def teamsJSON():
    return teamsJSONHandler(session)


# Show all sports categories
@app.route('/')
@app.route('/teams/')
def showTeams():
    return showTeamsHandler(session)


# Create a new sport entry
@app.route('/teams/new/', methods=['GET', 'POST'])
def newTeam():
    return newTeamHandler(session)


# Edit a Team
@app.route('/teams/<int:team_id>/edit/', methods=['GET', 'POST'])
def editTeam(team_id):
    return editTeamHandler(team_id, session)


# Delete a team
@app.route('/teams/<int:team_id>/delete/', methods=['GET', 'POST'])
def deleteTeam(team_id):
    return deleteTeamHandler(team_id, session)


# Show a teams batters
@app.route('/teams/<int:team_id>/')
@app.route('/teams/<int:team_id>/roster/')
def showRoster(team_id):
    return showRosterHandler(team_id, session)


# Create a new batter
@app.route('/teams/<int:team_id>/roster/new/', methods=['GET', 'POST'])
def newPlayer(team_id):
    return newPlayerHandler(team_id, session)


# Edit a batter's stats
@app.route('/teams/<int:team_id>/roster/<int:batter_id>/edit/',
           methods=['GET', 'POST'])
def editBatter(team_id, batter_id):
    return editBatterHandler(team_id, batter_id, session)


# Delete a batter
@app.route('/teams/<int:team_id>/roster/<int:batter_id>/delete/',
           methods=['GET', 'POST'])
def deleteBatter(team_id, batter_id):
    return deleteBatterHandler(team_id, batter_id, session)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
