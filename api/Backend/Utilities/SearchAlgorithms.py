class SearchAlgorithms:
    def binary_search(self, arr, target_id: int):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_id = arr[mid].get('id')

            if mid_id == target_id:
                return arr[mid]  # Found the object with the target ID
            elif mid_id < target_id:
                left = mid + 1
            else:
                right = mid - 1

        return None
