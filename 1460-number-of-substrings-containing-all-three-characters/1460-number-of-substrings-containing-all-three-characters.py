class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/solutions/6522736/sliding-window-python-c-java-js-c-go-rust-swift-kotlin/
        count = 0
        left = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        
        for right in range(len(s)):
            char_count[s[right]] += 1
            
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                count += len(s) - right
                char_count[s[left]] -= 1
                left += 1
        
        return count