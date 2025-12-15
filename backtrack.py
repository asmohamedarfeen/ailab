def calcSubset(A, res, subset, index):
    # Add the current subset to the result list
    res.append(subset[:])

    # Generate subsets by recursively including elements
    for i in range(index, len(A)):
        # Include the current element
        subset.append(A[i])

        # Recur for next elements
        calcSubset(A, res, subset, i + 1)

        # Exclude the current element (backtracking)
        subset.pop()


def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)
    return res


# Driver code
if __name__ == "__main__":
    array = [1, 2, 3]
    res = subsets(array)

    # Print the generated subsets
    for subset in res:
        print(*subset)
