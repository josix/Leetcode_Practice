class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        st = []
        while path_list != []:
            pos = path_list.pop(0)
            if st == [] and pos == "":
                st.append(pos)
            elif pos == "":
                pass
            elif pos == ".." and st[-1] == "":
                pass
            elif pos == ".":
                pass
            elif pos == "..":
                st.pop()
            else:
                st.append(pos)
        return "/".join(st) if len(st) > 1 else "/"
