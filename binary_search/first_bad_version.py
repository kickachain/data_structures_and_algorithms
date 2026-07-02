# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# brute force (linear seaarch)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        for i in range(1, n):
            if isBadVersion(i):
                return i
        return n
# Time Complexity: O(n)  
# Space Complexity: O(1)


# recursive binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def helper(l, r):
            if l > r:
                return l
            m = l + (r - l) // 2
            if isBadVersion(m):
                return helper(l, m - 1)
            else:
                return helper(m + 1, r)
        
        return helper(1, n)
# Time Complexity: O(log n)  
# Space Complexity: O(log n) for recursion stack


# iterative binary search
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
# Time Complexity: O(log n)  
# Space Complexity: O(1)


# iterative binary search (lower bound)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
# Time Complexity: O(log n)  
# Space Complexity: O(1)