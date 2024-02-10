from MidtermProject.ramdomNumberGenerator import RandomArrayGenerator
from MidtermProject.sortingAlgorithm import SortingAlgorithm
import time
import matplotlib.pyplot as plt
import numpy as np

datapoints = np.linspace(1000,100000, dtype=int, num=500)
randomArray = RandomArrayGenerator()
algorithm = SortingAlgorithm()

def executeSorting(randomArrayFunc):
    timeElapsed = {}
    timeElapsed['quickSort'] = []
    timeElapsed['heapSort'] = []
    timeElapsed['mergeSort'] = []
    timeElapsed['radixSort'] = []
    timeElapsed['bucketSort'] = []
    timeElapsed['timSort'] = []
    for points in datapoints:
        array = randomArrayFunc(points)

        t = time.time()
        algorithm.quickSort(array.copy())
        timeElapsed['quickSort'].append(time.time() - t)

        t = time.time()
        algorithm.heapSort(array.copy())
        timeElapsed['heapSort'].append(time.time() - t)

        t = time.time()
        algorithm.mergeSort(array.copy())
        timeElapsed['mergeSort'].append(time.time() - t)

        t = time.time()
        algorithm.radixSort(array.copy())
        timeElapsed['radixSort'].append(time.time() - t)

        t = time.time()
        algorithm.bucketSort(array.copy())
        timeElapsed['bucketSort'].append(time.time() - t)

        t = time.time()
        algorithm.timSort(array.copy())
        timeElapsed['timSort'].append(time.time() - t)
        array.clear()

    plt.plot(datapoints, timeElapsed['quickSort'], label='Quicksort')
    plt.plot(datapoints, timeElapsed['heapSort'], label='Heapsort')
    plt.plot(datapoints, timeElapsed['mergeSort'], label='Mergesort')
    plt.plot(datapoints, timeElapsed['radixSort'], label='Radixsort')
    plt.plot(datapoints, timeElapsed['bucketSort'], label='Bucketsort')
    plt.plot(datapoints, timeElapsed['timSort'], label='Timsort')
    plt.title("Sorting Alogrithms Analysis")
    plt.xlabel("Datapoints")
    plt.ylabel("Time taken")
    plt.legend(["Quicksort", "Heapsort", "Mergesort", "Radixsort", "Bucketsort", "Timsort"])
    plt.show()

executeSorting(randomArray.nRandom)
#executeSorting(randomArray.nRandomUpTo1000)
#executeSorting(randomArray.nRandomUpToNCube)
#executeSorting(randomArray.nRandomByLogValues)
#executeSorting(randomArray.nRandomMultiplesOf1000)
#executeSorting(randomArray.nRandomSwappedLogNBy2)



