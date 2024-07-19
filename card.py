#%%
# #pv : max 100 (spell max : 30)
#pa : points d'action - max 10 

class Card:

    def __init__(self, pa, damage = 0, position = 0):
        self.pa = pa
        self.damage = damage
        self.position = position


# attaque_tonette : Card(2, 3 ,4)
#%%

venom = Card(2, )


#%%
fireball = Card(5, 10, [(4,0),(4,-1),(4,1),(3,0),(5,0)]) # low impact, Impact --> ball

blizzard = Card(8, 20, [(1,0),(2,0),(3,0),(4,0),(5,0)]) # medium impact, line impact

tornado = Card(15,30,[(5,0),(5,-1),(5,1),(4,0),(6,0),]) # high impact, impact ball, diagonal line

rockfall = 

