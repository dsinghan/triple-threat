from game import Game
from team import Team
from utils import STARTING_TEAM

def main():
    team = Team(STARTING_TEAM)
    game = Game(team)
    game.display()

if __name__ == "__main__":
    main()