#%%


spells = {
    'attaque_tonnerre' : {'PA' : 1, 'Damage': 3}
}


class Card:

    def __init__(self, pa, damage = 0, position = 0):
        self.pa = pa
        self.damage = damage
        self.position = position


# attaque_tonette : Card(2, 3 ,4)
