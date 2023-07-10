# models

class Player:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Match:
    def __init__(self, player1, player2, result=None):
        self.player1 = player1
        self.player2 = player2
        self.result = result

class Round:
    def __init__(self, name, matches=None):
        self.name = name
        self.matches = matches or []

class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=None, players=None):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds or []
        self.players = players or []
