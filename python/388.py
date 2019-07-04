class Solution:
    def lengthLongestPath(self, input: str) -> int:
        path_list = input.split("\n")
        st = []
        max_length = 0
        for pos in path_list:
            level = pos.count('\t')
            # print(level)
            while len(st) - 1 >= level and st != []:
                st.pop()
            st.append(pos[level:])
            print(st)
            if '.' in pos:
                length = len("/".join(st))
                # print("/".join(st))
                max_length = max(length, max_length)
        return max_length
            
