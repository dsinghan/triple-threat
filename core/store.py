class Store:
    def __init__(self, gear=None, boosters=None):
        self.gear = gear if gear else []
        self.boosters = boosters if boosters else []

    def display(self):
        print("Available Gear:")
        for idx, gear in enumerate(self.gear):
            print(f"  {idx + 1}. {gear.name} - {gear.points} points - ${gear.cost}")
        print("Available Boosters:")
        for idx, booster in enumerate(self.boosters):
            print(f"  {idx + 1}. {booster.name} - {booster.points} points - ${booster.cost}")

    def get_item(self, category, idx):
        if category == 'gear' and 0 <= idx < len(self.gear):
            return self.gear[idx]
        elif category == 'booster' and 0 <= idx < len(self.boosters):
            return self.boosters[idx]
        return None

    def buy(self, item):
        if item in self.gear:
            self.gear.remove(item)
        elif item in self.boosters:
            self.boosters.remove(item)
