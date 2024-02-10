import random
import math
import numpy as np
from numpy.random import randint


class RandomArrayGenerator:

    """
    n randomly chosen integers in the range [0....n]
    """
    def nRandom(self, numberOfIntegers):
        return random.sample(range(0, numberOfIntegers), numberOfIntegers)

    """
    n randomly chosen integers in the range [0....k], k<1000
    """
    def nRandomUpTo1000(self, numberOfIntegers):
        return randint(0, 1000, numberOfIntegers).tolist()

    """
    n randomly chosen integers in the range [0....n^3]
    """
    def nRandomUpToNCube(self, numberOfIntegers):
        array = np.linspace(0, numberOfIntegers**3, num = numberOfIntegers, dtype=int)
        random.shuffle(array)
        return array.tolist()

    """
    n randomly chosen integers in the range [0....logn]
    """
    def nRandomByLogValues(self, numberOfIntegers):
        array = []
        for i in range(1,numberOfIntegers+1):
            array.append(math.log(i))
        random.shuffle(array)
        return array

    """
    n randomly chosen integers that are multiples of 1000 in the range [0....n]
    """
    def nRandomMultiplesOf1000(self, numberOfIntegers):
        return [random.randint(0, numberOfIntegers) * 1000 for _ in range(numberOfIntegers)]

    """
    the in order integers [0...n] where (log n)/2 randomly chosen values have been swapped with another value
    """
    def nRandomSwappedLogNBy2(self, numberOfIntegers):
        array = [i for i in range(numberOfIntegers)]
        numberOfSwaps = math.log(numberOfIntegers)/2
        while(numberOfSwaps>0):
            i = random.randint(0, numberOfIntegers-1)
            j = random.randint(0, numberOfIntegers-1)
            array[i], array[j] = array[j], array[i]
            numberOfSwaps -= 1

        return array


if __name__=="__main__":
    randomArrayGenerator = RandomArrayGenerator()
    print(randomArrayGenerator.nRandomSwappedLogNBy2(20))
