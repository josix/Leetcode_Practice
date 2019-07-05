
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        num = 0
        sign = 1
        st = []
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10*num + int(c)
            elif c == '-':
                sign = -1
            elif c == ',':
                if s[i-1] == ']':
                    continue
                st.append(sign*num)
                num = 0
                sign = 1
            elif c == '[':
                st.append(c)
            elif c == ']':
                # print('stack', st)
                if s[i - 1] != ']':
                    st.append(sign*num)
                list_ = []
                temp = st.pop()
                while temp != '[':
                    list_.append(temp)
                    temp = st.pop()
                    # print('list_', list_)
                if s[i - 1] == '[':
                    st.append([])
                elif list_ == []:
                    st.append(sign*num)
                else:
                    st.append(list_[::-1])
                    list_ = []
                num = 0
                sign = 1

        if st != []:
            return st[-1]
        else:
            return sign*num
