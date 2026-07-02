# first successful submission
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        final_output = []
        # while still values in list
        while strs:
            # first value in current list
            anchor = strs[0]
            # list of list first value
            anagrams = [anchor]
            # checks the remainder values in strs
            for word in strs[1:]:
                # checks if first value against renainder values is an anagram
                if self.is_anagram(anchor, word):
                    # append to current anagram list
                    anagrams.append(word)
            # we know weve seen the words in the anagram list so remove them from original list
            for word in anagrams:
                strs.remove(word)
            # append each anagram list to final output
            final_output.append(anagrams)
        return final_output

    def is_anagram(self, s: str, t: str) -> bool:
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
# what i learnt:
# recognise there is an efficient way with a certain pattern/data structure
# first solution too complex and inefficient
# dont just extend previous code, think about the problem from scratch

# need to go through this and comment code to understand it tomorrow
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())
