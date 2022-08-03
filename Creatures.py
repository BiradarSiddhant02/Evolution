import numpy as np
import math

class Creature:
    def __init__(self, N_wall = 0, S_wall = 0, E_wall = 0, W_wall = 0,
                 NE_corner = 0, NW_corner = 0, SE_corner = 0, SW_corner = 0,
                 up = 0, down = 0, right = 0, left = 0, lay_eggs = 0):
        
        self.N_wall = 0
        self.S_wall = 0
        self.E_wall = 0
        self.W_wall = 0
        
        self.NE_corner = 0
        self.NW_corner = 0
        self.SE_corner = 0
        self.SW_corner = 0
        
        # self.hungry = hungry
        # self.food_eaten = food_eaten
        
        self.up = 0
        self.right = 0
        self.left = 0
        self.down = 0
        
        self.node_index = {N_wall : 0,
                           S_wall : 1,
                           E_wall : 2,
                           W_wall : 3,
                           NE_corner : 4,
                           NW_corner : 5,
                           SE_corner : 6,
                           SW_corner : 7,
                        #    hungry : 8,
                        #    food_eaten : 9,
                        }
        self.movement = {up : 0,
                    right : 1,
                    left : 2,
                    down : 3,
                    lay_eggs : 4}                  
        
        # columns - nodes
        # rows - links 1 : connected 0 : not_connected
        
        
        # links = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #N_wall
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #S_wall
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #W_wall
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #E_wall
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #NE_corner
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #NW_corner
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #SE_corner
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #SW_corner
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],     #hungry
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],     #food_eaten
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #up
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #right
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #left
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #down
        #          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]     #lay_eggs
        
        # links = [[0, 0, 0, 0],      #N_wall
        #          [0, 0, 0, 0],      #S_wall
        #          [0, 0, 0, 0],      #W_wall
        #          [0, 0, 0, 0],      #E_wall
        #          [0, 0, 0, 0],      #NE_corner
        #          [0, 0, 0, 0],      #NW_corner
        #          [0, 0, 0, 0],      #SE_corner
        #          [0, 0, 0, 0]]      #SW_corner
        
        np.matrix([0, 0, 0, 0],     #N_wall
                  [0, 0, 0, 0],     #S_wall
                  [0, 0, 0, 0],     #W_wall
                  [0, 0, 0, 0],     #E_wall
                  [0, 0, 0, 0],     #NE_corner
                  [0, 0, 0, 0],     #NW_corner
                  [0, 0, 0, 0],     #SE_corner
                  [0, 0, 0, 0])     #SW_corner
        
        """
            mutation zone:
            links[0 : 9][10 : 14]
            links[8 : 10][15]
        """
    
    def get_distance():
        pass
        
    def hunger_level():
        pass
    
    def eat_food():
        pass
    
    def lay_eggs():
        pass
    
