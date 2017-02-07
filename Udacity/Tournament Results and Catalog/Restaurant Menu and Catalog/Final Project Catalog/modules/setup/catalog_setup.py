from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))

class Team(Base):
    __tablename__ = 'team'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    logo = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'user_id'      : self.user_id,
           'logo'         : self.logo,
       }
 
class Batter(Base):
    __tablename__ = 'batter'

    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    batting_average = Column(String(4))
    HR = Column(Integer)
    SB = Column(Integer)
    pos = Column(String(2))
    team_id = Column(Integer,ForeignKey('team.id'))
    team = relationship(Team)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'             : self.name,
           'position'         : self.pos,
           'batting average'  : self.batting_average,
           'id'               : self.id,
           'HR'               : self.HR,
           'SB'               : self.SB,
           'team_id'          : self.team_id,
           'user_id'          : self.user_id,
       }

engine = create_engine('sqlite:///teams.db')
 
Base.metadata.create_all(engine)
