from functools import lru_cache
from typing import List

class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        n = len(words)
        # 초기 문자열 = words[0]
        first0 = words[0][0]
        last0 = words[0][-1]
        # 남은 길이 (최소) 구하기: 첫 단어 길이 + 이후 추가 길이
        @lru_cache(None)
        def dp(i: int, first_char: str, last_char: str) -> int:
            # i는 다음 붙일 단어의 인덱스
            if i >= n:
                return 0
            w = words[i]
            f = w[0]
            l = w[-1]
            length_w = len(w)
            # 옵션1: 뒤에 붙이기 (current result + w)
            cost1 = length_w
            # 만약 겹치는 문자 가능 => 실제 추가 길이 = length_w − 1
            if f == last_char:
                cost1 -= 1
            # 이후 상태: first_char stays same, last_char becomes l
            cost1 += dp(i+1, first_char, l)
            # 옵션2: 앞에 붙이기 (w + current result)
            cost2 = length_w
            if l == first_char:
                cost2 -= 1
            # 이후 상태: first_char becomes f, last_char stays same
            cost2 += dp(i+1, f, last_char)
            # 최소 선택
            return min(cost1, cost2)

        return len(words[0]) + dp(1, first0, last0)