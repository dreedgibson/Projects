This is the project for the Udacity Catalog Project
This is a sports teams project.  

Configuration:
This project is run using python 2.7.13 supported with flask and SQLAlchemy

Installation:
The file contains folders modules, static, and templates
which contain all of the supporting code for the project.
Modules is a library of supporting python that contains the various handlers for the website. 

The secrets are needed for the app to properly authenticate via google and facebook
the database "teams.db" is created by running python catalog_setup.py
after navigating to this directory.  

to populate the database with a few teams and batters run 
python teamsandplayers.py

finally to launch the project run python catalogv2.py
and navigate to http://localhost:5000 to see the main page of the project.

Endpoints:
the following endpoints are available for public use:
http://localhost:5000
http://localhost:5000/teams
http://localhost:5000/teams/<int: team_id>/roster

The following JSON endpoints are also available
http://localhost:5000/teams/JSON
http://localhost:5000/teams/<int: team_id>/roster/JSON
http://localhost:5000/teams/<int: team_id>/roster/<int: batter_id>/JSON

Author:
Reed Gibson