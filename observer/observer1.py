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


class Player:
    def __init__(self, hero):
        self.hero = hero
        self.team = None

    def send_message(self, message):
        if self.team == 1:
            for player in War.team2:
                player.get_message(self, message)
        else:
            for player in War.team1:
                player.get_message(self, message)

    def get_message(self, sender, message):
        print(f"this is {self.hero} message tab, {sender.hero}: {message}")


sina = Player('Sina')
ali = Player('Ali')
reza = Player('Reza')
mohammad = Player('Mohammad')

war = War('map1', 'rainy')
war.join_players(sina)
war.join_players(ali)
war.join_players(reza)
war.join_players(mohammad)


sina.send_message('Hello to all')