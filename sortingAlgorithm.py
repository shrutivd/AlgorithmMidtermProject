from ramdomNumberGenerator import RandomArrayGenerator

class SortingAlgorithm():
    def quickSort(self, array):
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    (array[i], array[j]) = (array[j], array[i])
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            return i + 1

        def quickSortInternal(array, low, high):
            stack = [(0, len(array) - 1)]
            while stack:
                low, high = stack.pop()
                if low < high:
                    pivot_index = partition(array, low, high)
                    stack.append((low, pivot_index - 1))
                    stack.append((pivot_index + 1, high))
        quickSortInternal(array, 0, len(array)-1)

    def heapSort(self, array):
        def heapify(array, arrayLength, currentIndex):
            root = currentIndex
            left = 2 * currentIndex + 1
            right = 2 * currentIndex + 2

            if left < arrayLength and array[root] < array[left]:
                root = left

            if right < arrayLength and array[root] < array[right]:
                root = right

            if root != currentIndex:
                array[currentIndex], array[root] = array[root], array[currentIndex]
                heapify(array, arrayLength, root)

        arrayLength = len(array)

        for i in range(arrayLength // 2 - 1, -1, -1):
            heapify(array, arrayLength, i)

        for i in range(arrayLength - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, i, 0)


    def mergeSort(self, array):
        def merge(array, left, leftCount, right, rightCount):
            i = 0
            j = 0
            k = 0

            while (i < leftCount and j < rightCount):
                if (left[i] < right[j]):
                    array[k] = left[i]
                    i = i + 1
                else:
                    array[k] = right[j]
                    j = j + 1
                k = k + 1

            while (i < leftCount):
                array[k] = left[i]
                k = k + 1
                i = i + 1

            while (j < rightCount):
                array[k] = right[j]
                k = k + 1
                j = j + 1

        def mergeSortInternal(array):
            arrayLength = len(array)

            if (arrayLength < 2):
                return

            mid = arrayLength // 2

            left = array[:mid]
            right = array[mid:]

            mergeSortInternal(left)
            mergeSortInternal(right)

            merge(array, left, len(left), right, len(right))

        mergeSortInternal(array)

    def radixSort(self, array):
        def sort(array, exp_val):
            size = len(array)
            sorted_output = [0] * size
            occurrences = [0] * 10

            for i in range(size):
                index = array[i] // exp_val
                occurrences[int(index) % 10] += 1

            for i in range(1, 10):
                occurrences[i] += occurrences[i - 1]

            i = size - 1
            while i >= 0:
                index = array[i] // exp_val
                sorted_output[occurrences[int(index) % 10] - 1] = array[i]
                occurrences[int(index) % 10] -= 1
                i -= 1

            for i in range(size):
                array[i] = sorted_output[i]

        max_value = max(array)

        exp_value = 1
        while max_value // exp_value > 0:
            sort(array, exp_value)
            exp_value *= 10


    def bucketSort(self, array):
        def insertionSort(newArray):
            for i in range(1, len(newArray)):
                up = newArray[i]
                j = i - 1
                while j >= 0 and newArray[j] > up:
                    newArray[j + 1] = newArray[j]
                    j -= 1
                newArray[j + 1] = up
            return newArray

        if not array:
            return
        minimum = min(array)
        maximum = max(array)
        multiplier = 0
        if isinstance(array[0], int):
            multiplier = 1
        elif isinstance(array[0], float):
            multiplier = int(max(array) * 10)
        else:
            ValueError("Unsupported datatype")

        slot_num = int((maximum - minimum) * multiplier) + 1
        newArray = [[] for _ in range(slot_num)]
        for num in array:
            newArray[int((num - minimum) * multiplier)].append(num)
        for i in range(slot_num):
            newArray[i] = insertionSort(newArray[i])
        k = 0
        for i in range(slot_num):
            for j in range(len(newArray[i])):
                array[k] = newArray[i][j]
                k += 1


    def timSort(self, array):
        def calculateMinRun(arrayLength):
            run = 0
            while arrayLength >= 8:
                run |= arrayLength & 1
                arrayLength >>= 1
            return arrayLength + run

        def insertionSort(arr, left, right):
            for i in range(left + 1, right + 1):
                j = i
                while j > left and arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1

        def merge(array, left, mid, right):
            leftArrayLength = mid - left + 1
            rightArrayLength = right - mid
            leftArray = []
            rightArray = []
            for i in range(0, leftArrayLength):
                leftArray.append(array[left+i])
            for i in range(0, rightArrayLength):
                rightArray.append(array[mid + 1 + i])

            i, j, k = 0, 0, left

            while i < leftArrayLength and j < rightArrayLength:
                if leftArray[i] <= rightArray[j]:
                    array[k] = leftArray[i]
                    i += 1
                else:
                    array[k] = rightArray[j]
                    j += 1
                k += 1

            while i < leftArrayLength:
                array[k] = leftArray[i]
                k += 1
                i += 1

            while j < rightArrayLength:
                array[k] = rightArray[j]
                k += 1
                j += 1


        arrayLength = len(array)
        minRun = calculateMinRun(arrayLength)

        for start in range(0, arrayLength, minRun):
            end = min(start + minRun - 1, arrayLength - 1)
            insertionSort(array, start, end)

        size = minRun
        while size < arrayLength:

            for left in range(0, arrayLength, 2 * size):
                mid = min(arrayLength - 1, left + size - 1)
                right = min((left + 2 * size - 1), (arrayLength - 1))
                if mid < right:
                    merge(array, left, mid, right)

            size = 2 * size


if __name__=="__main__":
    arrayGenerator = RandomArrayGenerator()
    algorithm = SortingAlgorithm()
    array = arrayGenerator.nRandomByLogValues(10000)
    algorithm.bucketSort(array)
    array = arrayGenerator.nRandom(30000)
    algorithm.bucketSort(array)
