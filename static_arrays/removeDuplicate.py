# sorted set
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
# Time complexity: O(n log n)
# Space complexity: O(n)


# two pointers I
class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        # length of the array
        n = len(nums)
        # left and right pointers
        l = r = 0
        # while right pointer is less than the length of the array
        while r < n:
            # left pointer equals right pointer
            nums[l] = nums[r]
            # while right is less than length of array and right is the same as left
            while r < n and nums[r] == nums[l]:
                # increment right by 1 
                r += 1
            # increment left by 1 
            l += 1
        return l
# Time complexity: O(n)
# Space complexity: O(1)


# two pointers II
class Solution3:
    def removeDuplicates(self, nums: list[int]) -> int:
        # skip the start as it wont be a duplicate
        l = 1
        # loop through to the end of the array
        for r in range(1, len(nums)):
            # check the index is not the same as the previous number
            if nums[r] != nums[r - 1]:
                # if its not the same
                # replace the current value with the unique counter
                nums[l] = nums[r]
                # increment the counter
                l += 1
        # return the counter
        return l
# Time complexity: O(n)
# Space complexity: O(1)


# my solution
class Solution4(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [1,1,2]
        # counting unique numbers
        unique_index = 0
        # actual index
        # IMPORTANT whnever unique skip one if sorted, because first one is unique we can skip it (aka range, 1)
        for counter in range(1, len(nums)):
            # so we can skip the first 1 out of 1,1,2
            # so now we are only comparing 1,2
            if nums[counter] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[counter]
        return unique_index + 1

solution = Solution4()
solution = solution.removeDuplicates(nums=[1,1,5,5,7,7,8,8])
print(solution)

# notes
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         # nums = [1,1,2]
#         # counting unique numbers
#         unique_index = 1
#         # match the unique index with the range if skipping 1
#         # actual index
#         # IMPORTANT whnever unique skip one if sorted, because first one is unique we can skip it (aka range, 1)
#         for counter in range(1, len(nums)):
#             print(counter, 'counter')
#             # so we can skip the first 1 out of 1,1,4,4,4,5,7,7,9
#             # so now we are only comparing 1,4,4,4,5,7,7,9
#             if nums[counter] != nums[unique_index]:
#                 print(nums[counter], 'nums[counter]', nums[unique_index], 'nums[unique_index]')
                
#                 unique_index += 1
#                 nums[unique_index] = nums[counter]
#         print(unique_index)
#         return unique_index
    
# test = Solution()
# test.removeDuplicates([1,1, 4,4,4 ,5,7,7,9])