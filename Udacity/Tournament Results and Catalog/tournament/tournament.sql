-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drop the entire database if it exists to avoid error
DROP DATABASE IF EXISTS tournament;

-- Create the tournament database
CREATE DATABASE tournament;

-- Connect to the tournament database
\c tournament;

-- Create the player table
CREATE TABLE players (
	id serial PRIMARY KEY,
	name varchar(100)
	);

-- Create the matches table with foreign keys
CREATE TABLE matches (
	match_id serial PRIMARY KEY,
	winner int REFERENCES players (id),
	loser int REFERENCES players (id)
	);