class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_idx = {k:idx for idx, k in enumerate(order)}
        return ''.join(sorted(s, key = lambda x : order_idx.get(x, 27)))
        