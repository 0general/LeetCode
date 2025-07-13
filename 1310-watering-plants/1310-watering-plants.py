class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        amount = capacity
        for d, x in enumerate(plants):
            if amount < x:
                ans += 2 * d
                amount = capacity
            ans += 1
            amount -= x
        return ans