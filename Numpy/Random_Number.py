import numpy as np

rng=np.random.default_rng()

#print(rng.integers(0,50))
#print(rng.integers(low=0,high=50))
#print(rng.integers(low=0,high=50,size=3))
#print(rng.integers(low=0,high=50,size=(3,2)))
#print(np.random.rand(3))
#np.random.seed(seed=1)
#print(np.random.uniform(low=1,high=10))#floating number generate kore


#part2
rng2=np.random.default_rng()
#arr=np.array([1,2,3,4,5,6,7,8,9,10])
#rng.shuffle(arr)
#print(arr)

fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍇"])
#fruits=rng2.choice(fruits) #single element
fruits=rng2.choice(fruits,size=(3,3))
print(fruits)


