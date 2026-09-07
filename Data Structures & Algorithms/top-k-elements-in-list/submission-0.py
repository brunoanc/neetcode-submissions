class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ocurrences = {}

        for n in nums:
            ocurrences[n] = ocurrences.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, c in ocurrences.items():
            buckets[c].append(n)

        output = []
        added = 0

        for b in reversed(buckets):
            for n in b:
                output.append(n)
                added += 1

            if added >= k:
                break

        return output
