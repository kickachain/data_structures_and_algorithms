# interation two pass
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
# Time complexity: O(n)
# Space complexity: O(n)


# iteration one pass
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num
        return ans
# Time complexity: O(n)
# Space complexity: O(n)

# my answer
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # [1,2,1]
        # ans_size = len(nums) * 2 
        # ans = list(range(ans_size))
        # for num, an in zip(range(len(nums)), ans):
        ans = nums + nums
        return ans