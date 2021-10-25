import numpy as np
from math import pi, sin, cos, sqrt

import tqdm

import matplotlib.pyplot as plt

l1 = 1
l2 = 1
l3 = 1
l4 = 1



def J(q):
    """エンドエフェクター状態変数のヤコビ行列"""
    z = np.array([
        [
            -l1*sin(q[0,0]) + sqrt(2)*l2*cos(q[0,0] + q[1,0] + pi/4) + l2*cos(q[0,0] + q[0,0] + q[2,0]),
            l2*(sqrt(2)*cos(q[0,0] + q[2,0] + pi/4) + cos(q[0,0] + q[1,0] + q[2,0])),
            l2*cos(q[0,0] + q[1,0] + q[2,0])
        ],
        [
            l1*cos(q[0,0]) + sqrt(2)*l2*sin(q[0,0] + q[1,0] + pi/4) + l2*sin(q[0,0] + q[1,0] + q[2,0]),
            l2*(sqrt(2)*sin(q[0,0] + q[1,0] + pi/4) + sin(q[0,0] + q[1,0] + q[2,0])),
            l2*sin(q[0,0] + q[1,0] + q[2,0])
        ],
        [
            1,
            1,
            1,
        ],
    ])
    return z


def ee(q):
    x = l1*cos(q[0,0] + sqrt(2)*l2*sin(q[0,0] + q[1,0] + pi/4) + l2*sin(q[0,0] + q[1,0] + q[2,0]))
    y = l1*sin(q[0,0] - sqrt(2)*l2*cos(q[0,0] + q[1,0] + pi/4) - l2*cos(q[0,0] + q[1,0] + q[2,0]))
    phi = q[0,0] + q[1,0] + q[2,0] - 2*pi
    return np.array([[x, y, phi]]).T




xd = np.array([[
    3,
    0,
    pi/2
]]).T  # 目標値


def inv_kinema(xd, q_before=None):
    for j in tqdm.tqdm(range(10)):
        #print(j)
        if q_before is None:
            q =  [np.random.rand()*2*pi for k in range(3)]
            q = np.array([q]).T
        
        else:
            q = q_before
        
        for i in range(100):
            
            x = ee(q)
            error = xd - x # 誤差
            
            dq = np.linalg.pinv(J(q)) @ error
            
            q = q + 0.1 * dq
        
        if np.linalg.norm(xd[0:2, :] - x[0:2, :]) < 0.01:
            if abs(xd[2, 0] - x[2, 0]) < 0.000001:
                #print(j, "で成功!!")
                break
    
    return q


if __name__ == '__main__':
    def D1(q):
        return np.array([
            [cos(q[0,0]), -sin(q[0,0]), 0],
            [sin(q[0,0]), cos(q[0,0]), 0],
            [0, 0, 1],
        ])

    def D2(q):
        return np.array([
            [1, 0, l1],
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
            [1, 0, l2],
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
            [1, 0, l3],
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
            [1, 0, l4],
            [0, 1, 0],
            [0, 0, 1],
        ])

    D_func_all = [D1, D2, D3, D4, D5, D6, D7, D8]




if __name__ == "__main__":
    q = np.zeros((7,1))
    temp_ee = ee(q)

    print(q)

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.scatter(temp_ee[0, 0], temp_ee[1, 0], label = 'sol')
    ax.scatter(xd[0, 0], xd[1, 0], marker = '*', s=500, label = 'desired')

    ax.grid(True)

    D_all = [Di(q) for Di in D_func_all]

    for j, D in enumerate(D_all):
        if j == 0:
            D_w_all = [D]
        else:
            D_w_all.append(D_w_all[j-1] @ D)

    x = []
    y = []
    for D in D_w_all:
        x.append(D[0, 2])
        y.append(D[1, 2])

    ax.plot(x, y, label='leg')

    for j, D_w in enumerate(D_w_all):
        ax.scatter(
            D_w[0, 2], D_w[1, 2], label = str(j+1),
        )




    ax.legend()


    ax.set_aspect('equal')
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    plt.show()

