from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x = random.normal(size=(2, 3))
x = random.normal(loc=1, scale=2, size=(2, 3)) #mean =1, SD = 2

print(x)

sns.distplot(random.normal(size=1000), hist=False)

plt.show()