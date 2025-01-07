class Player():
    def __init__(self):
        self.gravity = 3
        self.move_speed = 5
        self.location = (20,500)
        self.player_hearts = 3
    def collider_check(self):