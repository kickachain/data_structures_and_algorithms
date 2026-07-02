# brute force
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)
# Time complexity: O(n)
# Space complexity: O(n)


# two pointer I
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
# Time complexity: O(n)
# Space complexity: O(1)


# two pointer II
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n
# Time complexity: O(n)
# Space complexity: O(1)

# my solution
class Solution(object):
    def removeElement(self, nums, val):
        duplicate_counter = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[duplicate_counter] = nums[index]
                duplicate_counter += 1
        return duplicate_counter