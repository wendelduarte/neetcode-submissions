class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        response = []
        count = Counter(nums)
        for i in range(k):
            max_key = max(count, key=count.get)
            response.append(max_key)
            del count[max_key]
        return response