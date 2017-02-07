from ..setup.catalog_setup import Base, Team, Batter, User
from flask import session as login_session


# get the user id from the email
def getUserID(email, session):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# get user info by the user id
def getUserInfo(user_id, session):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# create a new user in the database
def createUser(login_session, session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id
