
class Solution:
    def selectionSort(self, arr):
        n = len(arr)

        for i in range(n):
            min_index = i

            # Find minimum in remaining array
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


# Example
arr = [64, 25, 12, 22, 11]
sol = Solution()
print(sol.selectionSort(arr))