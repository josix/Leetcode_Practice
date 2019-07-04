class Solution:
    def decodeString(self, s: str) -> str:
        st = [["", 1 ,""]]
        a = n = ""
        for letter in s:
            if letter.isdigit():
                n += letter
            elif letter.isalpha():
                a += letter
            elif letter == '[':
                st.append([a, int(n), ''])
                a = n = ""
            elif letter == "]":
                last_str, last_k, last_ans = st.pop()
                st[-1][-1] += last_str + last_k * (last_ans + a)
                a = ""
        return st[-1][-1] + a
