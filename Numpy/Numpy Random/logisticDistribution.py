from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.logistic(loc=1, scale=2, size=(2, 3)) #used for growth generally
#Used extensively in machine learning in logistic regression, neural networks etc.
#loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array.
print(x)

sns.distplot(random.logistic(size=1000), hist=False)
plt.show()