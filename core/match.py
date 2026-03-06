class Match:
    def __init__(self, team, opponent):
        self.team = team
        self.opponent = opponent

    def play(self):
        team_score = self.team.get_points()
        opponent_score = self.opponent.points
        if team_score > opponent_score:
            return "Team wins!"
        elif team_score < opponent_score:
            return "Opponent wins!"
        else:
            return "It's a tie!"
