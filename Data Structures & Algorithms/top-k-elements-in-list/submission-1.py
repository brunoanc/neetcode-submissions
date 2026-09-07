class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}

        for n in nums:
            occurrences[n] = occurrences.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, c in occurrences.items():
            buckets[c].append(n)

        output = []
        added = 0

        for b in reversed(buckets):
            for n in b:
                output.append(n)
                added += 1

            if len(output) == k:
                return output
