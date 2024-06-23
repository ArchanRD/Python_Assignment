def search(nums: list[int], target: int, start, end) -> int:
    if target in nums:
        if start > end:
            return -1

        mid = start + (end - start ) // 2
        if target == nums[mid]:
            return mid
        elif target > mid:
            start = mid + 1
            return search(nums, target, start, end)
        else:
            end = mid - 1
            return search(nums, target, start, end)

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(search(nums, target,0, len(nums)-1))