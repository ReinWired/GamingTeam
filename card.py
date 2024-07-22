#%%
import random
#pv : max 100 (spell max : 30)
#pa : max 10 

class Card:
    list_spells = []

    def __init__(self, name, pa, damage = 0, position = 0):
        self.name = name
        self.pa = pa
        self.damage = damage
        self.position = position
        Card.list_spells.append(name)

    @staticmethod
    def shuffle_3():
        return random.choices(Card.list_spells, k=3)
    
    @staticmethod
    def shuffle_1():
        return random.choice(Card.list_spells)
    

class Attack:
    def __init__(self, start, duration):
        self.start = start
        self.duration = duration


#%% spells

venom = Card('venom', 2, 10, [(4, 0), (4, -1), (4, 1), (5, 0), (3, 0), (2, 0), (6, 0)])

swords = Card('swords', 3, 15, [(2, 0), (2, -1), (2, 1), (3, 0), (3, -1), (3, 1), (4, 0)])

fireball = Card('fireball', 5, 10, [(4,0),(4,-1),(4,1),(3,0),(5,0)]) # low impact, Impact --> ball

blizzard = Card('blizzard', 8, 20, [(1,0),(2,0),(3,0),(4,0),(5,0)]) # medium impact, line impact

tornado = Card('tornado', 10,30,[(5,2),(5,1),(5,3),(4,2),(6,2),(6,3),(6,1),(4,3),(4,1),(3,4),(3,0),(7,4),(7,0)]) # high impact, impact ball, diagonal line

rockfall = Card('rockfall', 9,15,[(2,0),(2,1),(2,2),(2,3),(2,4),(2,-1),(2,-2),(2,-3)])

ice_throw = Card('ice_throw', 2,2,[(6,0)])

lane_fire = Card('lane_fire', 4, 8, [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)])

tsunami = Card('tsunami', 5, 12, [(1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2)])

sun_burn = Card('sun_burn', 4, 10, [(3, 0), (3, -1), (3, 1), (4, 0), (5, 0)])


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



place((0,0), tsunami.position)

# %%

print(Card.shuffle_3())

# %%
print(Card.list_spells)