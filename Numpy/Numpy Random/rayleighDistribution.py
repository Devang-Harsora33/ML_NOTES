from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.rayleigh(scale=2, size=(2, 3))
#Rayleigh distribution is used in signal processing.
#scale - (standard deviation) decides how flat the distribution will be default 1.0).
# size - The shape of the returned array.

print(x)

sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()