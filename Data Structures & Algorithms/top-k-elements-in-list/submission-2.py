from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        c = Counter(nums)
        c_most = c.most_common(k)
        for i in range(k):
            output.append(c_most[i][0])
        return output
