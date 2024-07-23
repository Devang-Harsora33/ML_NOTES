from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.pareto(a=2, size=(2, 3))
#A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
#a - shape parameter.
# size - The shape of the returned array.
print(x)

sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()