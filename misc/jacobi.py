import sympy as sy
from sympy import pi, cos, sin, tan


q1 = sy.Symbol("q1")
q2 = sy.Symbol("q2")
q3 = sy.Symbol("q3")

qvec = sy.Matrix([[q1, q2, q3,]]).T


l1 = sy.Symbol("l1")
l2 = sy.Symbol("l2")
l3 = sy.Symbol("l2")
l4 = sy.Symbol("l2")



D1 = sy.Matrix([
        [cos(q1), -sin(q1), 0.0],
        [sin(q1), cos(q1), 0.0],
        [0.0, 0.0, 1.0],
    ])

D2 = sy.Matrix([
        [1.0, 0.0, l1],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])

D3 = sy.Matrix([
        [cos(q2), -sin(q2), 0.0],
        [sin(q2), cos(q2), 0.0],
        [0.0, 0.0, 1.0],
    ])

D4 = sy.Matrix([
        [1.0, 0.0, l2],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])


theta = 270/180*pi
D5 = sy.Matrix([
        [cos(theta), -sin(theta), 0.0],
        [sin(theta), cos(theta), 0.0],
        [0.0, 0.0, 1.0],
    ])

D6 = sy.Matrix([
        [1.0, 0.0, l3],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])

D7 = sy.Matrix([
        [cos(q3), -sin(q3), 0.0],
        [sin(q3), cos(q3), 0.0],
        [0.0, 0.0, 1.0],
    ])

D8 = sy.Matrix([
        [1.0, 0.0, l4],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ])


D_end = D1 * D2 * D3 * D4 * D5 * D6 * D7 * D8
D_end = sy.simplify(D_end)


phi = sy.Symbol('phi')


ee = sy.Matrix([
    [D_end[0, 2]],
    [D_end[1, 2]],
    [phi]
])

jacobi = ee.jacobian(qvec)

jacobi = sy.simplify(jacobi)
print(jacobi)