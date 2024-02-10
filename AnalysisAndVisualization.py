from ramdomNumberGenerator import RandomArrayGenerator
from sortingAlgorithm import SortingAlgorithm
import time
import matplotlib.pyplot as plt
import numpy as np

datapoints = np.linspace(1000, 100000, dtype=int, num=10)
randomArray = RandomArrayGenerator()
algorithm = SortingAlgorithm()

def executeSorting(randomArrayFunc, graphTitle="Sorting Algorithm Analysis"):
    timeElapsed = {}
    timeElapsed['quickSort'] = []
    timeElapsed['heapSort'] = []
    timeElapsed['mergeSort'] = []
    timeElapsed['radixSort'] = []
    timeElapsed['bucketSort'] = []
    timeElapsed['timSort'] = []
    for points in datapoints:
        array = randomArrayFunc(points)

        t = time.perf_counter()
        algorithm.quickSort(array.copy())
        timeElapsed['quickSort'].append((time.perf_counter() - t) * 1_000)

        t = time.perf_counter()
        algorithm.heapSort(array.copy())
        timeElapsed['heapSort'].append((time.perf_counter() - t) * 1_000)

        t = time.perf_counter()
        algorithm.mergeSort(array.copy())
        timeElapsed['mergeSort'].append((time.perf_counter() - t) * 1_000)

        t = time.perf_counter()
        algorithm.radixSort(array.copy())
        timeElapsed['radixSort'].append((time.perf_counter() - t) * 1_000)

        t = time.perf_counter()
        algorithm.bucketSort(array.copy())
        timeElapsed['bucketSort'].append((time.perf_counter() - t) * 1_000)

        t = time.perf_counter()
        algorithm.timSort(array.copy())
        timeElapsed['timSort'].append((time.perf_counter() - t) * 1_000)
        array.clear()

    plt.clf()
    plt.plot(datapoints, timeElapsed['quickSort'], label='Quicksort')
    plt.plot(datapoints, timeElapsed['heapSort'], label='Heapsort')
    plt.plot(datapoints, timeElapsed['mergeSort'], label='Mergesort')
    plt.plot(datapoints, timeElapsed['radixSort'], label='Radixsort')
    plt.plot(datapoints, timeElapsed['bucketSort'], label='Bucketsort')
    plt.plot(datapoints, timeElapsed['timSort'], label='Timsort')
    plt.legend(loc="upper left")
    plt.title(graphTitle)
    plt.xlabel("Datapoints")
    plt.ylabel("Time taken (milliseconds)")
    plt.savefig(str(time.time())+".png")
    print("Done!: ", graphTitle)

#executeSorting(randomArray.nRandom, "n randomly chosen integers in the range [0....n]")
#executeSorting(randomArray.nRandomUpTo1000, "n randomly chosen integers in the range [0....k], k<1000")
executeSorting(randomArray.nRandomUpToNCube, "n random integers in the range [0....n^3] (including bucketSort)")
#executeSorting(randomArray.nRandomByLogValues, "n randomly chosen integers in the range [0....logn]")
executeSorting(randomArray.nRandomMultiplesOf1000, "multiples of 1000 in the range [0....n] (including bucketSort)")
#executeSorting(randomArray.nRandomSwappedLogNBy2, "integers [0...n] where (log n)/2 randomly swapped")



