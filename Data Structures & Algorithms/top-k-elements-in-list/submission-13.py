class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        reversed_counter = collections.defaultdict(list)
        res = []

        for key, value in dict(counter).items():
            reversed_counter[value].append(key)

        for count in range(len(nums), -1, -1):
            if k == 0:
                return res

            if reversed_counter[count]:
                for num in reversed_counter[count]:
                    res.append(num)
                    k -= 1