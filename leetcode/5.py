### 最长回文子串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        start = 0
        
        for i in range(n):  # 遍历所有中心点（奇数回文：i 为中心；偶数回文：i 和 i+1 之间）
            # 1. 处理奇数长度回文（中心在 i）
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # 扩展后，回文长度 = right - left - 1
            if right - left - 1 > max_len:
                max_len = right - left - 1
                start = left + 1  # 起始位置
            
            # 2. 处理偶数长度回文（中心在 i 和 i+1）
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > max_len:
                max_len = right - left - 1
                start = left + 1
        
        return s[start:start + max_len]