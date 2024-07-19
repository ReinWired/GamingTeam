#%%

#pv : max 100 (spell max : 30)
#pa : max 10 

class Card:

    def __init__(self, pa, damage = 0, position = 0):
        self.pa = pa
        self.damage = damage
        self.position = position

#%% spells

venom = Card(2, 10, [(4, 0), (4, -1), (4, 1), (5, 0), (3, 0), (2, 0), (6, 0)])

swords = Card(3, 15, [(2, 0), (2, -1), (2, 1), (3, 0), (3, -1), (3, 1), (4, 0)])


#%%
fireball = Card(5, 10, [(4,0),(4,-1),(4,1),(3,0),(5,0)]) # low impact, Impact --> ball

blizzard = Card(8, 20, [(1,0),(2,0),(3,0),(4,0),(5,0)]) # medium impact, line impact

tornado = Card(10,30,[(5,2),(5,1),(5,3),(4,2),(6,2),(6,3),(6,1),(4,3),(4,1),(3,4),(3,0),(7,4),(7,0)]) # high impact, impact ball, diagonal line

rockfall = Card(9,15,[(2,0),(2,1),(2,2),(2,3),(2,4),(2,-1),(2,-2),(2,-3)])

ice_throw = Card(2,2,[(6,0)])

lane_fire = Card(4, 8, [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])

tsunami = Card(5, 12, [(1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)])

sun_burn = Card(4, 10, [(3, 0), (3, -1), (3, 1), (4, 0), (5, 0)])


#%% for testing

map = [[' ' for _ in range(10)] for _ in range(5)]

def affiche_map():
    for i in map:
        print(i)

def place(pos, spell):
    for i in spell:
        try :
            map[pos[1] + i[1]][pos[0] + i[0]] = 'X'
        except:
            pass
    map[pos[1]][pos[0]] = 'O'
    affiche_map()



place((0,0), ice_throw.position)

# %%
