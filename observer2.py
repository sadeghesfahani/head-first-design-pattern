import math


class War:
    team1 = []
    team2 = []

    def __init__(self, map_name, weather):
        self.map_name = map_name
        self.weather = weather

    @staticmethod
    def join_players(player):
        if len(War.team1) >= len(War.team2):
            War.team2.append(player)
            player.team = 2
        else:
            War.team1.append(player)
            player.team = 1

    @staticmethod
    def player_moves(player):
        print(f'{player.hero} moves to {player.position}')
        for team1_player in War.team1:
            team1_player.process_nearby_players(player)
        for team2_player in War.team2:
            team2_player.process_nearby_players(player)


class Player:
    def __init__(self, hero):
        self.hero = hero
        self.team = None
        self.position = [0, 0]
        self.nearby_players = []

    def send_chanel_message(self, message):
        if self.team == 1:
            for player in War.team2:
                player.get_message(self, message)
        else:
            for player in War.team1:
                player.get_message(self, message)

    def send_nearby_message(self, message):
        for player in self.nearby_players:
            player.get_message(self, message)

    def get_message(self, sender, message):
        print(f"this is {self.hero} message tab, {sender.hero}: {message}")

    def move(self, position):
        self.position = position
        War.player_moves(self)

    @staticmethod
    def calculation_distance(position1, position2):
        return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

    def process_nearby_players(self, player):
        if self.calculation_distance(self.position, player.position) < 5:
            self.nearby_players.append(player)
        else:
            try:
                self.nearby_players.remove(player)
            except ValueError:
                pass


sina = Player('Sina')
ali = Player('Ali')
reza = Player('Reza')
mohammad = Player('Mohammad')
sara = Player('Sara')
mahnaz = Player('Mahnaz')
samira = Player('Samira')
maryam = Player('Maryam')


war = War('map1', 'rainy')
war.join_players(sina)
war.join_players(ali)
war.join_players(reza)
war.join_players(mohammad)
war.join_players(sara)
war.join_players(mahnaz)
war.join_players(samira)
war.join_players(maryam)

sina.move([100, 100])
ali.move([20, 20])
reza.move([3, 3])
mohammad.move([4, 4])
sara.move([5, 5])
mahnaz.move([6, 6])
samira.move([7, 7])
maryam.move([8, 8])


maryam.send_nearby_message('Hello to all')