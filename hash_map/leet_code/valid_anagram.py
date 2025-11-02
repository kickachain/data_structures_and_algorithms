# my solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # gatekeep technique
        # not equals length can't be anagram return False
        if len(t) != len(s):
            return False

        # hashmaps to compare
        inc = self.increment_counts_of_characters

        if inc(s) == inc(t):
            return True
        else:
            return False

    @staticmethod
    def increment_counts_of_characters(word):
        # create hashmap
        word_map = {}
        # loop through characters
        for character in word:
            # hashmap of characters with a count added and incremented for each character, or set default value
            word_map[character] = word_map.get(character, 0) + 1
        return word_map


# neetcode solution
# Hash Table (Using Array)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1


        for val in count:
            if val != 0:
                return False
        return True
# hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}


        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
# sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
