from core.game import Game
from models.team import Team
from data.constants import STARTING_TEAM

def main():
    team = Team(STARTING_TEAM)
    game = Game(team, 100)
    game.display()

if __name__ == "__main__":
    main()