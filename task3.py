import numpy as np
import matplotlib.pyplot as plt

interval = (2.8, 4)  # start, end
accuracy = 0.0001
reps = 600  # number of repetitions
numtoplot = 200
lims = np.zeros(reps)

fig, biax = plt.subplots()
fig.set_size_inches(16, 9)


lyap=[]

lims[0] = np.random.rand()
for r in np.arange(interval[0], interval[1], accuracy):
    res = []
    for i in range(reps - 1):
        lims[i + 1] = r * lims[i] * (1 - lims[i]) +0.01*(lims[i]**4)
        #r * np.sin(lims[i]*np.pi)
        #r * lims[i] * (1 - lims[i])
        #r * lims[i] * (1 - lims[i]) +0.01*(lims[i]**4)
        if(i>399):
            res.append(np.log(abs(r-2*r*lims[i] + 0.04*(lims[i]**3))))
    #lyap.append(np.mean(res))
    lyap = np.mean(res)
    biax.plot([r] * numtoplot, lims[reps - numtoplot :], "b.", markersize=0.02)
    biax.plot(r, lyap, "g.", markersize=1)

biax.set(xlabel="r", ylabel="x", title="logistic map")
plt.show()

