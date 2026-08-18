from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        common = counts.most_common(k)
        result = [pair[0] for pair in common]
        return result