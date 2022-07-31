class Creature:
    def __init__(self, N_wall, S_wall, E_wall, W_wall,
                 NE_corner, NW_corner, SE_corner, SW_corner,
                 hungry, food_eaten, node_index, up, down, right, left, lay_eggs):
        
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
                           up : 10,
                           right : 11,
                           left : 12,
                           down : 13,
                           lay_eggs : 14}
        
        # columns - nodes
        # rows - links 1 : connected 0 : not_connected
        
        
        links = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #N_wall
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #S_wall
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #W_wall
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #E_wall
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #NE_corner
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #NW_corner
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #SE_corner
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],     #SW_corner
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],     #hungry
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],     #food_eaten
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #up
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #right
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #left
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],     #down
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]     #lay_eggs
        
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
    
