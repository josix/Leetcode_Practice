class Solution:
    def simplifyPath(self, path: str) -> str:
        from collections import deque
        path_list = deque([pos for pos in path.split('/') if pos != "" and pos != "."])
        st = [""]
        while len(path_list) != 0:
            pos = path_list.popleft()
            if st == [] and pos == "":
                st.append(pos)
            elif pos == "..":
                if st[-1] != "":
                    st.pop()
            else:
                st.append(pos)
        return "/".join(st) if len(st) > 1 else "/"
                
            
        
