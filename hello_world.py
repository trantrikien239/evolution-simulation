# This will set up a world
import numpy as np
from random import random
import logging
from datetime import datetime


class World():
    def __init__(self, length = 200, life_forms = None, life_existed = None):
        self.abs_coor = length / 2
        if life_forms is None:
            self.life_forms = []
        else:
            self.life_forms = life_forms
        if life_existed is None:
            self.life_existed = []
        else:
            self.life_existed = life_existed

    def pop(self):
        return(len(self.life_forms))

    def add_life(self, lifo):
        if lifo not in self.life_forms:
            self.life_forms.append(lifo)
            self.life_existed.append(lifo)

    def remove_life(self,lifo):
        if lifo in self.life_forms:
            self.life_forms.remove(lifo)
            lifo.is_alive = False

class Life():
    def __init__(self, world, coordinate = None):
        self.is_alive = True 
        if coordinate is None:
            self.coordinate = np.random.randint(0 - world.abs_coor, world.abs_coor + 1)
        world.add_life(self)

# class Blob(Life):
#     def __init__(self, world, coordinate = None, color = 'Blue'):
#         super().__init__(world, coordinate)
#         self.color = color
def stime(world, num_day, world_func, life_func, log_func): 
    # stime = simulated time
    print('Start simulation for {} days'.format(num_day))
    for day in range(num_day):
        world_func(world)
        for life in world.life_forms:
            life_func(world, life)
        if day % 10 == 0:
            # Some kind of logging function here
            log_func(world, day)

    print('Simulation of {} days completed'.format(num_day))

def main():
    NUM_DAY = 2000
    BORN_RATE = 0.5
    REPRODUCE_RATE = 0.005
    DIE_RATE = 0.01
    
    logging.info('Initializing a new world named Earth ...')
    Earth = World()
    Lives = []
    cnt_popup = 0
    cnt_rprd = 0
    cnt_death = 0
    logging.info('And now, {} days begin'.format(NUM_DAY))
    for i in range(NUM_DAY):
        x = random()
        if x < BORN_RATE:
            Lives.append(Life(Earth))
            cnt_popup += 1
        for life in Lives:
            if life.is_alive:
                y = random()
                z = random()
                if y < DIE_RATE:
                    life.is_alive = False
                    Earth.remove_life(life)
                    cnt_death += 1
                if z < REPRODUCE_RATE:
                    Lives.append(Life(Earth))
                    cnt_rprd += 1
        if i % 50 == 0:
            logging.info(f'Day: {i} | Population: {Earth.pop()} | Popup: {cnt_popup} | Death: {cnt_death} | Reproduction: {cnt_rprd}')

    logging.info('\n=============>>> Simulation ends!\n')
    logging.info('Number of Lives have ever lived: {}'.format(len(Lives)))
    logging.info('Current population: {}'.format(Earth.pop()))

if __name__ == '__main__':
    time_start = datetime.now()
    logging.basicConfig(filename = 'log/hello_world.log',\
                        level=logging.DEBUG,\
                        format='%(message)s')
    logging.info('Script started running at: {}'.format(time_start))
    main()
    time_stop = datetime.now()
    logging.info('Script stopped running at: {}\nTotal run time: {}\n=============================\n\n'.format(time_stop, time_stop - time_start))