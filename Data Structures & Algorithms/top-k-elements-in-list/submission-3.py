from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        c = Counter(nums)
        c_most = c.most_common(k)
        for pair in c_most:
            output.append(pair[0])
        return output
