from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.poisson(lam=2, size=10)
#lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array.

print(x)
sns.distplot(random.poisson(lam=2, size=1000), kde=False)
plt.show()
sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
plt.show()



sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')
plt.show()
