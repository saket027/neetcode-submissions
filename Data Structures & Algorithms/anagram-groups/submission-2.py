from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We can call a word an anagram if cintains the exact same characters as the another string.
        # So the brute force approach would be to first iterate over each word in the given list and then sort it
        # After sorting check for the same words in the list then group them.
        countmap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            countmap[tuple(count)].append(s)
        return list(countmap.values())