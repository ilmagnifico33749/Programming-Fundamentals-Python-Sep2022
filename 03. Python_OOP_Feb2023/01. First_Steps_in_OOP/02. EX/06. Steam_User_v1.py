
class SteamUser:
    def __init__(self, username, games, played_hours=0):
        self.username = str(username)
        self.games = list(games)
        self.played_hours = int(played_hours)

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.games)} games. Total play time: {self.played_hours}"


# ############################################################
# Test_Code_1:
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
# -----------------------------------------------------------
# Output_1:
# Peter is playing Fortnite
# Oxygen Not Included is not in library
# CS:GO is already in your library
# Peter bought Oxygen Not Included
# Peter is playing Oxygen Not Included
# Peter has 4 games. Total play time: 9
# ############################################################
