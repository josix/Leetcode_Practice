class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = [pos for pos in path.split('/') if pos != "" and pos != "."]
        st = [""]
        while path_list != []:
            pos = path_list.pop(0)
            if st == [] and pos == "":
                st.append(pos)
            elif pos == "..":
                if st[-1] != "":
                    st.pop()
            else:
                st.append(pos)
        return "/".join(st) if len(st) > 1 else "/"
