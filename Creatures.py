import Nodes
import numpy as np
import math
import random as rd

class Creature:
    def __init__(self, N_wall = 0, W_wall = 0, S_wall = 0, E_wall = 0,
                 NE_corner = 0, NW_corner = 0, SW_corner = 0, SE_corner = 0,
                 x_pos = 0, y_pos = 0, width = 10, height = 10):
        
        self.N_wall = N_wall
        self.S_wall = S_wall
        self.E_wall = E_wall
        self.W_wall = W_wall
        
        self.NE_corner = NE_corner
        self.NW_corner = NW_corner
        self.SE_corner = SE_corner
        self.SW_corner = SW_corner
        
        # self.hungry = hungry
        # self.food_eaten = food_eaten
        
        up = 0
        right = 0
        left = 0
        down = 0
        
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
                         down : 3}                  
        
        self.x_pos = rd.randint(0, 1366)
        self.y_pos = rd.randint(0, 720)
        self.width = 10
        self.height = 10
        
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
        
        links = ([0, 0, 0, 0],     #N_wall
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
            
            (ignore)
        """
    
    # def get_distance():
    #     pass
        
    # def hunger_level():
    #     pass
    
    # def eat_food():
    #     pass
    
    # def lay_eggs():
    #     pass
    

    
    
