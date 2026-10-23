from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            anagrams[tuple(sorted_word)].append(word)
        return list(anagrams.values())