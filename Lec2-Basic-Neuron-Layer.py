i = [2.1, 1.2, 3.6, 4.8]

w1 = [0.1, 0.5, -0.2, 1.0]
w2 = [0.2, -0.8, 0.61, -0.45]
w3 = [-0.38, 0.5, -0.2, 0.6]

b1 = 2.0
b2 = 3.0
b3 = 0.5

output = [ i[0]*w1[0] + i[1]*w1[1] + i[2]*w1[2] + i[3]*w1[3] + b1,
           i[0]*w2[0] + i[1]*w2[1] + i[2]*w2[2] + i[3]*w2[3] + b2,
           i[0]*w3[0] + i[1]*w3[1] + i[2]*w3[2] + i[3]*w3[3] + b3 ]

print(output)