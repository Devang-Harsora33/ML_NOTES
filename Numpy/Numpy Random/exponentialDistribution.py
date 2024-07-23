from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=(2, 3))
#Exponential distribution is used for describing time till next event e.g. failure/success etc.
#scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size - The shape of the returned array.

print(x)

sns.distplot(random.exponential(size=1000), hist=False)
plt.show()