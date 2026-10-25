from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count = Counter(nums)
        most = count.most_common(k)
        print(most)
        for i in most:
            output.append(i[0])
        return output