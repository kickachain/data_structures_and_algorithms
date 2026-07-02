# queue solution
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        res = n
        for sandwich in sandwiches:
            cnt = 0
            while cnt < n and q[0] != sandwich:
                cur = q.popleft()
                q.append(cur)
                cnt += 1

            if q[0] == sandwich:
                q.popleft()
                res -= 1
            else:
                break
        return res
# Time Complexity: O(2ⁿ)
# Space Complexity: O(n)


# iteration
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        idx = 0

        res = n
        for sandwich in sandwiches:
            cnt = 0
            while cnt < n and students[idx] != sandwich:
                idx += 1
                idx %= n
                cnt += 1

            if students[idx] == sandwich:
                students[idx] = -1
                res -= 1
            else:
                break
        return res
# Time Complexity: O(n2)
# Space Complexity: O(1)


# frequency count
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s] > 0:
                res -= 1
                cnt[s] -= 1
            else:
                break
        
        return res
# Time Complexity: O(n)
# Space Complexity: O(1)