from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.uniform(size=(2, 3))#Used to describe probability where every event has equal chances of occuring.s
print(x)

sns.distplot(random.uniform(size=1000), hist=False)
plt.show()