class Solution:
    def hashmap(self, s):
        map = {}
        for i in s:
            if i not in map:
                map[i] = 0
            map[i] += 1
        return map
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = self.hashmap(s)
        t_hashmap = self.hashmap(t)
        return s_hashmap == t_hashmap