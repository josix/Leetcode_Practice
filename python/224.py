class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        num = 0
        ans = 0
        sign = 1
        for c in s:
            if c != ' ':
                if c.isdigit():
                    num = 10 * num + int(c)
                elif c == '+' or c == '-':
                    ans += sign*num
                    num = 0
                    sign = 1 if c == '+' else -1
                elif c == '(':
                    st.append((ans, sign))
                    ans = 0
                    sign = 1
                elif c == ')':
                    ans += sign*num
                    last_ans, last_sign = st.pop()
                    ans = last_ans + last_sign * ans
                    num = 0
        return ans + sign*num
                    
                
