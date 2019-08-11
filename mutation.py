from hello_world import Life, World, stime
import random as rd
from random import random
import logging

class Blob(Life):
    DATA ={
        'blue':{
            'BORN_RATE': 0.5,
            'REPRODUCE_RATE': 0.005,
            'DIE_RATE': 0.01,
            'MUT_RATE':0.2,
            'MUT_CHOICE':['green','red']
        },
        'green':{
            'BORN_RATE': 0.0,
            'REPRODUCE_RATE': 0.005,
            'DIE_RATE': 0.01,
            'MUT_RATE':0.0,
            'MUT_CHOICE':['']
        },
        'red':{
            'BORN_RATE': 0.0,
            'REPRODUCE_RATE': 0.005,
            'DIE_RATE': 0.005,
            'MUT_RATE':0.05,
            'MUT_CHOICE':['orange']
        },
        'orange':{
            'BORN_RATE': 0.0,
            'REPRODUCE_RATE': 0.01,
            'DIE_RATE': 0.005,
            'MUT_RATE':0.0,
            'MUT_CHOICE':['']
        }
    }

    def __init__(self, world, coordinate = None, color = 'blue'):
        super().__init__(world,coordinate)
        self.color = color
        self.born_rate = self.DATA[self.color]['BORN_RATE']
        self.reproduce_rate = self.DATA[self.color]['REPRODUCE_RATE']
        self.die_rate = self.DATA[self.color]['DIE_RATE']
        self.mut_rate = self.DATA[self.color]['MUT_RATE']
        self.mut_choice = self.DATA[self.color]['MUT_CHOICE']

    def __repr__(self):
        return 'A {} blob, born {}, repr {}, die {}, mut {}, mut choice {}'\
            .format(self.color,
                    self.born_rate,
                    self.reproduce_rate,
                    self.die_rate,
                    self.mut_rate,
                    self.mut_choice
                    )

def world_func(world):
    born = random()
    if born < Blob.DATA['blue']['BORN_RATE']:
        world.add_life(Blob(world))
    return world

def life_func(world, blob):
    die = random()
    reproduce = random()
    mutate = random()
    if reproduce < blob.reproduce_rate:
        if mutate < blob.mut_rate:
            world.add_life(Blob(world, color=rd.choice(blob.mut_choice)))
        else:
            world.add_life(Blob(world, color=blob.color))
    if die < blob.die_rate:
        world.remove_life(blob)
    
def world_log(world, day):

    colors = [blob.color for blob in world.life_forms]
    pop = {}
    for x in colors:
        if x in pop:
            pop[x] += 1
        else:
            pop[x] = 1
    
    print('Day: {}, Existing: {}, Total existed: {}'.format(day, len(world.life_forms), len(world.life_existed)), str(pop))






def main():
    earth = World()
    stime(earth, 2000, world_func = world_func, life_func = life_func, log_func = world_log)


if __name__ == '__main__':
    main()
    