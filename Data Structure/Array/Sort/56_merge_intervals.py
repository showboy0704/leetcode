def quicksort(data, left, right):
    if left >= right:
        return

    i = left
    j = right
    key = data[left]

    while i != j:
        while data[j][0] > key[0] and i < j:
            j -= 1
        while data[i][0] <= key[0] and i < j:
            i += 1
        if i < j:
            data[i], data[j] = data[j], data[i]

    data[left] = data[i]
    data[i] = key

    quicksort(data, left, i-1)
    quicksort(data, i+1, right)


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        quicksort(intervals, 0, len(intervals)-1)

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            left, right = result[-1]
            l, r = intervals[i]
            if left <= r <= right:
                continue
            elif right < l:
                result.append(intervals[i])
            elif left <= l <= right:
                result[-1][1] = r

        return result


if __name__ == '__main__':
    intervals = [[1, 4], [4, 5]]
    print(f"{intervals}")
    print('----------Answer Below----------')
    print(Solution().merge(intervals))
