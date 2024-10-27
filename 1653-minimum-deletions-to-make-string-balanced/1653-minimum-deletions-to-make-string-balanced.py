class Solution:
    def minimumDeletions(self, s: str) -> int:
        # b를 삭제하는게 나은지 a 를 삭제하는게 나은지 계산한다. 
        # 참고 : https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/discuss/5925114/One-Pass-and-O(1)-Space-or-Greedy-or-Beats-100-or-Most-Efficient-or-Explained-or-C%2B%2B-or-Java.
        b_count = 0
        min_del = 0
        for letter in s:
            if letter == 'a':
                # 최소 숫자 정하기 : 지금까지 삭제한 것에서 a 를 추가로 삭제하든가, 지금까지의 b를 모두 삭제하든가
                min_del = min(min_del + 1, b_count)
            else:
                b_count += 1
        return min_del