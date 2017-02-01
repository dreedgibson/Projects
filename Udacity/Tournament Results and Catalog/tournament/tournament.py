#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""

    try:
        DB = psycopg2.connect("dbname=tournament")
        cursor = DB.cursor()
        return DB, cursor
    except:
        print "I am unable to connect to database"


def deleteMatches():
    """Remove all the match records from the database."""

    # attempt to connect to the database and create cursor
    DB, cursor = connect()

    # delete matches table
    cursor.execute("TRUNCATE matches;")

    # commit change to database
    DB.commit()

    # close connection
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""

    # attempt to connect to the database and create cursor
    DB, cursor = connect()

    # delete players
    cursor.execute("TRUNCATE players CASCADE;")

    # commit change to database
    DB.commit()

    # close connection
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""

    # attempt to connect to the database and create cursor
    DB, cursor = connect()

    # count players
    cursor.execute("SELECT COUNT(*) AS num_players FROM players;")
    count = cursor.fetchone()

    # close connection
    DB.close()

    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    # attempt to connect to the database and create cursor
    DB, cursor = connect()

    # create insert query
    query = ("INSERT INTO PLAYERS (name) VALUES (%s);")

    # insert name into table
    cursor.execute(query, (name,))

    # commit change to database
    DB.commit()

    # close connection
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    # attempt to connect to the database and create cursor
    DB, cursor = connect()

    # define win and loss query
    qw = ("SELECT players.id, players.name, count(matches.winner) " +
          "AS wins FROM players LEFT JOIN matches ON matches.winner =" +
          "players.id GROUP BY players.id ORDER BY wins DESC, id ASC;")

    # gather losses
    ql = ("SELECT count(matches.loser) " +
          "AS losses FROM players LEFT JOIN matches ON matches.loser =" +
          "players.id GROUP BY players.id ORDER BY losses ASC, id ASC;")

    # get wins and losses tables
    cursor.execute(qw)
    sql_wins = cursor.fetchall()

    cursor.execute(ql)
    sql_losses = cursor.fetchall()

    # close connection
    DB.close()

    # create standings list
    standings = []

    # populate standings list
    for i in xrange(len(sql_losses)):
        standings.append((sql_wins[i][0], sql_wins[i][1],
                          sql_wins[i][2], (sql_losses[i][0] + sql_wins[i][2])))

    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    # attempt to connect to the database and create cursor
    DB, cursor = connect()

    # create win and loss queries
    q = "INSERT INTO matches VALUES (%s, %s);"

    # record outcome of match
    cursor.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s);",
                   (winner, loser))

    # commit changes to database
    DB.commit()

    # close connection
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # get standings
    standings = playerStandings()

    # declare list of matches
    matches = []

    # populate matches
    for i in xrange(0, countPlayers(), 2):
        matches.append((standings[i][0], standings[i][1],
                        standings[i + 1][0], standings[i + 1][1]))

    return matches
