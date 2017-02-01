from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
from sqlalchemy import func

from puppies import Base, Shelter, Puppy
import datetime

engine = create_engine('sqlite:///puppyshelter.db')

# bind engine to base class
Base.metadata.bind = engine

# create sessionmaker object
DBSession = sessionmaker(bind=engine)

# create session
session = DBSession()

# # query all puppies and return ordered by puppy name
# all_puppies = session.query(Puppy).order_by(Puppy.name).all()

# for puppy in all_puppies:
# 	print puppy.dateOfBirth

# # query all puppies less than 6 months old order by youngest first
# today = datetime.date.today()
# query_date = today - datetime.timedelta(days = 180)

# young_puppies = session.query(Puppy).filter(Puppy.dateOfBirth > query_date).order_by(desc(Puppy.dateOfBirth)).all()

# for puppy in young_puppies:
# 	print puppy.dateOfBirth

# # query all puppies by weight ascending
# fat_puppies = session.query(Puppy).order_by(Puppy.weight).all()

# for puppy in fat_puppies:
# 	print str(puppy.weight) + " " + puppy.name

# query all puppies grouped by shelter in which they are staying
shelter_puppies = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()

for item in shelter_puppies:
	print item[0].name, item[1] 

