### 字符串转换整数 (atoi)

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

# 自动机，状态量s会根据a(输入字符)转移
# 有点像动态规划
class Automaton:
    def __init__(self):
        self.state = 'start'  # 初始状态名
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    # 获取该次输入字符，从而找到状态转移Table的列数
    def get_col(self, c):
        if c.isspace():  # 记一下这两个api isspace(), isdigit()
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    # 根据规则转移
    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            # 直接用整型的操作，不要再用''.join(chars)后转化
            self.ans = self.ans * 10 + int(c)
            # 直接用min()，这样简单
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans