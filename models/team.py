from models.player import Player
from models.support import Support


class Team:
    def __init__(self, data):
        self.name = data["name"]
        self.budget = data.get("budget", 100)
        players = data.get("players", {})
        self.guard = Player(players["guard"]) if "guard" in players else None
        self.forward = Player(players["forward"]) if "forward" in players else None
        self.center = Player(players["center"]) if "center" in players else None
        support = data.get("support", {})
        self.coach = Support(support["coach"]) if "coach" in support else None
        self.superfan = Support(support["superfan"]) if "superfan" in support else None

    def add_player(self, player):
        if player.position == "guard":
            self.guard = player
        elif player.position == "forward":
            self.forward = player
        elif player.position == "center":
            self.center = player

    def add_support(self, support):
        if support.name == "coach":
            self.coach = support
        elif support.name == "superfan":
            self.superfan = support

    def score(self):
        return (self.guard.points if self.guard else 0) + \
               (self.forward.points if self.forward else 0) + \
               (self.center.points if self.center else 0) + \
               (self.coach.points if self.coach else 0) + \
               (self.superfan.points if self.superfan else 0)
