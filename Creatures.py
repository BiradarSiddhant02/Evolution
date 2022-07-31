class Creature:
    def __init__(self, N_wall, S_wall, E_wall, W_wall,
                 NE_corner, NW_corner, SE_corner, SW_corner,
                 hungry, food_eaten, eggs_laid, node_index, up, down, right, left):
        
        self.N_wall = N_wall
        self.S_wall = S_wall
        self.E_wall = E_wall
        self.W_wall = W_wall
        
        self.NE_corner = NE_corner
        self.NW_corner = NW_corner
        self.SE_corner = SE_corner
        self.SW_corner = SW_corner
        
        self.hungry = hungry
        self.food_eaten = food_eaten
        self.eggs_laid = eggs_laid
        
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
                           hungry : 8,
                           food_eaten : 9,
                           eggs_laid : 10,
                           up : 11,
                           right : 12,
                           left : 13,
                           down : 14}
    
    def get_distance():
        pass
        
    def hunger_level():
        pass
    
    def eat_food():
        pass
    
    def lay_eggs():
        pass
    
