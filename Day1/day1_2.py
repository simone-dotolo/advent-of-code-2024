def binary_search(arr, target, left_most=True):
    left = 0
    right = len(arr) - 1

    ans = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            ans = mid
            if left_most:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return ans

with open('input.txt') as f:
    lines = f.readlines()

    list_1 = [int(el.split()[0]) for el in lines]
    list_2 = [int(el.split()[1]) for el in lines]

    list_2.sort()

    res = 0

    for i in range(len(list_1)):
        left_index = binary_search(list_2, list_1[i], left_most=True)
        right_index = binary_search(list_2, list_1[i], left_most=False)
        if left_index != -1 and right_index != -1:
            n_occ = right_index - left_index + 1
            res += n_occ * list_1[i]

    print(res)
