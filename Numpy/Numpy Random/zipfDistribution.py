from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=(2, 3))
#Zipf distributions are used to sample data based on zipf's law.
#Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. 
# E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
# a - distribution parameter.
# size - The shape of the returned array.

print(x)

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)
plt.show()