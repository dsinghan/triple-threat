from core.match import Match


class Game:
    def __init__(self, team, budget):
        self.team = team
        self.budget = budget

    def play_match(self, opponent):
        match = Match(self.team, opponent)
        result = match.play()
        print(result)

    def shop_store(self, store):
        while True:
            store.display()
            print(f"Budget: ${self.budget}")
            choice = input("\nEnter command (e.g. 'buy gear 1', 'buy booster 2', 'exit'): ").strip().lower()
            if choice == 'exit':
                return
            parts = choice.split()
            if len(parts) != 3 or parts[0] != 'buy':
                print("Invalid command.")
                continue
            category = parts[1]
            try:
                idx = int(parts[2]) - 1
            except ValueError:
                print("Invalid number.")
                continue
            item = store.get_item(category, idx)
            if not item:
                print("Invalid choice.")
            elif self.budget < item.cost:
                print("Not enough budget.")
            else:
                self.budget -= item.cost
                store.buy(item)
                self.team.add_item(item)
                print(f"Bought {item.name}.")

    def run_game(self):
        pass

    def display(self):
        print(f"Team: {self.team.name}")
        print(f"Budget: ${self.budget}")
        print(f"Guard: {self.team.guard.name if self.team.guard else 'None'}")
        print(f"Forward: {self.team.forward.name if self.team.forward else 'None'}")
        print(f"Center: {self.team.center.name if self.team.center else 'None'}")
        print(f"Coach: {self.team.coach.name if self.team.coach else 'None'}")
        print(f"Superfan: {self.team.superfan.name if self.team.superfan else 'None'}")
        print(f"Total Points: {self.team.get_points()}")
        print("Items in Bag:")
        for item in self.team.bag:
            print(f"  {item.name} - {item.points} points - ${item.cost}")
