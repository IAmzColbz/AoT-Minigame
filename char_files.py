class Enemy:
    """A simple enemy class that defines normal and abnormal titans"""
    def __init__(self, nape_cut, height, agility, durability, speed):
        self.nape_cut = nape_cut
        self.height = height
        self.agility = agility
        self.durability = durability
        self.speed = speed

# nape_cut set to true is the win condition as that declares the titan dead
# Height is self explanitory and is in meters. 
# Agility is their hit chance, think of their ability to grab.
# durability is the kill chance of a nape strike 1 being weak, 10 being the strongest possible.
# speed defines the titans ability to catch you if you attempt to flee, 1 being slow, 10 being the fastest possible 

class Abnormal(Enemy):
    def __init__(self):
        super().__init__()

titan = Enemy(
    nape_cut = False,
    height = 15,
    agility = 5,
    durability = 10,
    speed = 2
)
