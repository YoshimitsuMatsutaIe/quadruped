import numpy as np
from math import pi, cos, sin, tan


class Positions:
    x = []
    y = []
    z = []

    def add(self, X):
        self.x.append(X[0, 0])
        self.y.append(X[1, 0])
        self.z.append(X[2, 0])



class LegKinematics:
    """足の運動学"""
    l1 = 1
    l2 = 1
    l3 = 1
    l4 = 1
    
    def __init__(self, name):
        self.name = name
        
        
        def D1(self, q):
            return np.array([
                [cos(q[0,0]), -sin(q[0,0]), 0],
                [sin(q[0,0]), cos(q[0,0]), 0],
                [0, 0, 1],
            ])

        def D2(q):
            return np.array([
                [1, 0, self.l1],
                [0, 1, 0],
                [0, 0, 1],
            ])

        def D3(q):
            return np.array([
                [cos(q[1,0]), -sin(q[1,0]), 0],
                [sin(q[1,0]), cos(q[1,0]), 0],
                [0, 0, 1],
            ])

        def D4(q):
            return np.array([
                [1, 0, self.l2],
                [0, 1, 0],
                [0, 0, 1],
            ])

        def D5(q):
            theta = 270/180*pi
            return np.array([
                [cos(theta), -sin(theta), 0],
                [sin(theta), cos(theta), 0],
                [0, 0, 1],
            ])

        def D6(q):
            return np.array([
                [1, 0, self.l3],
                [0, 1, 0],
                [0, 0, 1],
            ])

        def D7(q):
            return np.array([
                [cos(q[2,0]), -sin(q[2,0]), 0],
                [sin(q[2,0]), cos(q[2,0]), 0],
                [0, 0, 1],
            ])

        def D8(q):
            return np.array([
                [1, 0, self.l4],
                [0, 1, 0],
                [0, 0, 1],
            ])

        self.D_func_all = [D1, D2, D3, D4, D5, D6, D7, D8]
    
    
    def get_joint_positions(self, q):
        positions = Positions()
        for i, D in enumerate(self.D_func_all):
            if i == 0:
                D_w = D(q)
            else:
                D_w = D_w @ D(q)
        positions.add(D_w[0:2, 2:3])
        return positions


if __name__ == '__main__':
    pass
