import numpy as np
import math

class Node:
    def __init__(self, weight, bias, link):
        self.weight = weight
        self.bias = bias
        self.link = link
       
    def get_value(value):
        return value   
        
    def output(self, weight, link, bias, value):
        z = weight * value + bias
        return math.sigmoid(z)