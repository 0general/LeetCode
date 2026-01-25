class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(map({*allowed}.issuperset, words))