class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # 마지막으로 마신 음료가 A / B 일 때 최대 상태
        dpA = dpB = 0
        for a, b in zip(energyDrinkA, energyDrinkB):
            newA = max(dpA + a, dpB)
            newB = max(dpB + b, dpA)
            dpA, dpB = newA, newB
        return max(dpA, dpB)