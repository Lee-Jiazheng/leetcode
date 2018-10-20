def partition(arr, left, right, pivot):
    # 比pivot小的放左边，大的放右边
    storeI = left
    storeV = arr[pivot]
    arr[pivot], arr[right] = arr[right], arr[pivot]

    for i in range(left, right):
        if storeV < arr[i]:
            arr[i], arr[storeI] = arr[storeI], arr[i]
            storeI += 1
    
    arr[right], arr[storeI] = arr[storeI], arr[right]
    #print(arr, left, right, storeI)
    return storeI

def findKMax(arr, left, right, K):
    nPos = partition(arr, left, right, left)

    if nPos < K:
        return findKMax(arr, nPos+1, right, K)
    elif nPos > K:
        return findKMax(arr, left, nPos-1, K)
    return arr[nPos]

if __name__ == "__main__":
    l, k = list(map(int, input().strip().split()))
    nums = list(map(int, input().strip().split()))
    print(findKMax(nums, 0, l-1, k-1))
#partition([0, 2, 4, 1, 3], 0, 4, 1)
#findKMax([0, 2, 4, 1, 3], 0, 4, 1)