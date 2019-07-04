class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        num = 0
        st = []
        for c in s:
            if c != ' ':
                if c.isdigit():
                    num = 10 * num + int(c)
                    continue
                if sign == "+":
                    st.append(num)
                elif sign == "-":
                    st.append(-1*num)
                elif sign == "*":
                    st.append(num*st.pop())
                elif sign == "/":
                    operand = st.pop()
                    if operand < 0:
                        st.append(-1*(abs(operand)//num))
                    else:
                        st.append(operand//num)
                sign = c
                num = 0
        if sign == '*':
            st.append(num*st.pop())
        elif sign == "/":
            operand = st.pop()
            if operand < 0:
                st.append(-1*(abs(operand)//num))
            else:
                st.append(operand//num)
        elif sign == '+':
            st.append(num)
        elif sign == '-':
            st.append(-1*num)
        return sum(st)
