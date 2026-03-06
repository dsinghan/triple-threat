class Player:
    def __init__(self, player_info):
        self.name = player_info.get("name")
        self.position = player_info.get("position")
        self.points = player_info.get("points", 0)
        self.gear = None

    def equip_gear(self, gear):
        if self.gear:
            self.points -= self.gear.points
        self.points += gear.points
        self.gear = gear