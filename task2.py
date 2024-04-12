import numpy as np
# delta = 4.669201
periods = 11
m=[None]*periods
m[0] = 1.9975
m[1]= 3.2449
delta = [None]*periods
delta[1] = 5
x0=1/2
xp0=0

derivs=[]

for n in range(2, periods):
    #if n==1:

    m[n]=m[n-1] + (m[n-1]-m[n-2])/delta[n-1]

    for _ in range(20):
        for i in range(2**n):
            x = m[n] * x0 * (1 - x0) + 0.01*(x0**4)
            xp = x0 * (1 - x0) + m[n] * xp0 * (1 - 2 * x0)
            x0 = x
            xp0 = xp
        derivs.append(xp)
        u = m[n] - (x - 1 / 2) / xp
        m[n] = u
    #print(m)
    delta[n] = (m[n-1] - m[n-2]) / (m[n] - m[n-1])

print(delta)
#print(4.6577838075395634/(derivs[-1]/derivs[-2]))
'''
change superstable point to 5
get m2 from first iteration?
'''
# import numpy as np
# # delta = 4.669201
# periods = 11
# m=[None]*periods
# m[0] = 2
# m[1]= 1+np.sqrt(5)
# delta = [None]*periods
# delta[1] = 5
# x0=1/2
# xp0=0
#
# derivs=[]
#
# for n in range(2, periods):
#     m[n]=m[n-1] + (m[n-1]-m[n-2])/delta[n-1]
#
#     for _ in range(10):
#         for i in range(2**n):
#             x = m[n] * x0 * (1 - x0) + 0.01*(x0**4)
#             xp = x0 * (1 - x0) + m[n] * xp0 * (1 - 2 * x0)
#             x0 = x
#             xp0 = xp
#         derivs.append(xp)
#         u = m[n] - (x - 1 / 2) / xp
#         m[n] = u
#
#     #print(m)
#     delta[n] = (m[n-1] - m[n-2]) / (m[n] - m[n-1])
#
# print(delta)
# print(4.6577838075395634/(derivs[-1]/derivs[-2]))
