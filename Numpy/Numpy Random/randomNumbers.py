from numpy import random
import numpy as np

randomNumber = random.randint(100)
randomFloat = random.rand() #between 0 to 1
randomShape = random.rand(5)
randomShape2 = random.rand(3, 5)
randomChoice = random.choice([1,2,3,4]) #1D
randomChoice2 = random.choice([3, 5, 7, 9], size=(3, 5)) #2D
randomArray =random.randint(100, size=(5)) #1D
randomArray2 =random.randint(100, size=(3, 5)) #2D
DataDistribution = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(4))
DataDistribution2 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr) # make changes to original arr


print(randomNumber)
print(randomFloat)
print(randomShape)
print(randomShape2)
print(randomChoice)
print(randomChoice2)
print(randomArray)
print(randomArray2)
print(DataDistribution)
print(DataDistribution2)
print(arr)
print(random.permutation(arr)) #no original is shuffled

