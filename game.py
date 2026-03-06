class Game:
    def __init__(self, team):
        self.team = team

    def display(self):
        print(f"Team: {self.team.name}")
        print(f"Budget: ${self.team.budget}")
        print(f"Guard: {self.team.guard.name if self.team.guard else 'None'}")
        print(f"Forward: {self.team.forward.name if self.team.forward else 'None'}")
        print(f"Center: {self.team.center.name if self.team.center else 'None'}")
        print(f"Coach: {self.team.coach.name if self.team.coach else 'None'}")
        print(f"Superfan: {self.team.superfan.name if self.team.superfan else 'None'}")
        print(f"Total Points: {self.team.score()}")