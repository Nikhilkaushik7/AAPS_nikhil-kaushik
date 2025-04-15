class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0

        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)

            target = ans | (1 << i)
            for prefix in prefixes:
                if (target ^ prefix) in prefixes:
                    ans = target
                    break

        return ans
        
