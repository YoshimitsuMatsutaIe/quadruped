import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
from math import pi, cos, sin, tan



import invkinema


# 同時変換行列

l1 = 1
l2 = 1
l3 = 1
l4 = 1

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


# 図示
class Hoge:
    
    
    def __init__(self,):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # global q
        # q = np.array([[60, -60, 60]]).T * pi/180

        # D_all = [Di(q) for Di in D_func_all]

        # for j, D in enumerate(D_all):
        #     if j == 0:
        #         D_w_all = [D]
        #     else:
        #         D_w_all.append(D_w_all[j-1] @ D)

        # x = []
        # y = []
        # for D in D_w_all:
        #     x.append(D[0, 2])
        #     y.append(D[1, 2])



        # for j, D_w in enumerate(D_w_all):
        #     ax.scatter(
        #         D_w[0, 2], D_w[1, 2], label = str(j+1),
        #     )

        ax.legend()
        ax.grid(True)


        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)


        time_template = 'time = %s [epoch]'
        ax.text(-0.5, -1, time_template % 0, size = 10)


        self.q =  [np.random.rand()*2*pi for k in range(3)]
        self.q = np.array([self.q]).T

        def update(i):
            
            ax.cla()
            print(i)
            
            xd = np.array([[2.8, 0.01*i-1, pi/2]]).T
            
            
            if i == 0:

                self.q = invkinema.inv_kinema(xd)
            else:
                self.q = invkinema.inv_kinema(xd, self.q)

            
            D_all = [Di(self.q) for Di in D_func_all]

            D_w_all = []
            for j, D in enumerate(D_all):
                if j == 0:
                    D_w_all.append(D)
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
            ax.grid(True)
            
            ax.text(-0.5, -1, time_template % i, size = 10)
            
            ax.set_aspect('equal')
            ax.set_xlim(-3, 3)
            ax.set_ylim(-3, 3)

            return

        ani = anm.FuncAnimation(
            fig = fig,
            func = update,
            frames = 100,
        )

        ani.save('hoge.gif')

        plt.show()


if __name__ == '__main__':
    hoge = Hoge()