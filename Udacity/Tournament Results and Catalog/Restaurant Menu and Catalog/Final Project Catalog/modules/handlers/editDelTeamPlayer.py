from flask import Flask, render_template, flash, request, redirect, url_for
from flask import session as login_session
from ..functions.userfunctions import getUserInfo
from ..setup.catalog_setup import Base, Team, Batter, User


# Edit a Team
def editTeamHandler(team_id, session):
    # ensure someone is logged in prior for editing priveleges
    if 'username' not in login_session:
        return redirect('/login')
    # get correct team from database
    teamToEdit = session.query(Team).filter_by(id=team_id).one()
    # ensure user is authorized to edit team
    if teamToEdit.user_id != login_session['user_id']:
        return ("<script>function myFunction() {alert('Not authorized" +
        " to edit this team.');}</script><body onload='myFunction()'>")
    # save edits to database
    if request.method == 'POST':
        if request.form['name']:
            teamToEdit.name = request.form['name']
            session.add(teamToEdit)
            session.commit()
            flash('Team Successfully Edited %s' % teamToEdit.name)
            return redirect(url_for('showTeams'))
    else:
        return render_template('editteam.html', team=teamToEdit)


# Delete a team
def deleteTeamHandler(team_id, session):
    # ensure someone is logged to allow deleting priveleges
    if 'username' not in login_session:
        return redirect('/login')
    # query database for team to delete
    teamToDelete = session.query(Team).filter_by(id=team_id).one()
    # ensure user is authorized to delete team
    if teamToDelete.user_id != login_session['user_id']:
        return ("<script>function myFunction() {alert('Not authorized" +
        "to delete this team.');}</script><body onload='myFunction()'>")
    # delete team and save database
    if request.method == 'POST':
        session.delete(teamToDelete)
        flash('%s Successfully Deleted' % teamToDelete.name)
        session.commit()
        return redirect(url_for('showTeams'))
    else:
        return render_template('deleteteam.html', team=teamToDelete)


# edit a batter
def editBatterHandler(team_id, batter_id, session):
    # ensure someone is logged in prior to allowing editing priveleges
    if 'username' not in login_session:
        return redirect('/login')
    # query database for team and batter to edit
    batterToEdit = session.query(Batter).filter_by(id=batter_id).one()
    team = session.query(Team).filter_by(id=team_id).one()
    # ensure user is authorized to edit batter
    if team.user_id != login_session['user_id']:
        return ("<script>function myFunction() {alert('Not authorized" +
        " to edit this batter.');}</script><body onload='myFunction()'>")
    # edit batter and commit to databases
    if request.method == 'POST':
        if request.form['name']:
            batterToEdit.name = request.form['name']
        if request.form['BA']:
            batterToEdit.batting_average = request.form['BA']
        if request.form['HR']:
            batterToEdit.HR = request.form['HR']
        if request.form['SB']:
            batterToEdit.SB = request.form['SB']
        if request.form['pos']:
            batterToEdit.pos = request.form['pos']
        session.add(batterToEdit)
        session.commit()
        flash('Player stats successfully edited')
        return redirect(url_for('showRoster', team_id=team_id))
    else:
        return render_template('editbatter.html', team_id=team_id,
                               batter_id=batter_id, batter=batterToEdit)


# delete a batter
def deleteBatterHandler(team_id, batter_id, session):
    # ensure a user is logged in
    if 'username' not in login_session:
        return redirect('/login')
    # query database for batter to delete
    batterToDelete = session.query(Batter).filter_by(id=batter_id).one()
    team = session.query(Team).filter_by(id=team_id).one()
    # ensure user has authorization
    if batterToDelete.user_id != login_session['user_id']:
        return ("<script>function myFunction() {alert('Not authorized" +
        " to delete this player.');}</script><body onload='myFunction()'>")
    # delete batter and commit changes
    if request.method == 'POST':
        session.delete(batterToDelete)
        session.commit()
        flash('Player Successfully Deleted')
        return redirect(url_for('showRoster', team_id=team_id))
    else:
        return render_template('deletebatter.html', batter=batterToDelete)


# new player
def newPlayerHandler(team_id, session):
    # ensure user is logged in 
    if 'username' not in login_session:
        return redirect('/login')
    # query database for team
    team = session.query(Team).filter_by(id=team_id).one()
    # ensure user is authorized to add players
    if team.user_id != login_session['user_id']:
        return ("<script>function myFunction() {alert('Not authorized" +
        " to add players to roster.');}</script><body onload='myFunction()'>")
    # create new batter and commit to database
    if request.method == 'POST':
        newBatter = Batter(name=request.form['name'],
                           batting_average=request.form['BA'],
                           HR=request.form['HR'],
                           SB=request.form['SB'],
                           pos=request.form['pos'],
                           team_id=team_id,
                           user_id=team.user_id)
        session.add(newBatter)
        session.commit()
        flash('New Batter %s Successfully Created' % (newBatter.name))
        return redirect(url_for('showRoster', team_id=team_id))
    else:
        return render_template('newbatter.html', team_id=team_id)


# new team
def newTeamHandler(session):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newTeam = Team(name=request.form['name'],
                       logo=request.form['logo'],
                       user_id=login_session['user_id'])
        session.add(newTeam)
        flash('New Team %s Successfully Created' % newTeam.name)
        session.commit()
        return redirect(url_for('showTeams'))
    else:
        return render_template('newteam.html')
