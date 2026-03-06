class Support:
    def __init__(self, support_info):
        self.name = support_info.get("name")
        self.points = support_info.get("points", 0)