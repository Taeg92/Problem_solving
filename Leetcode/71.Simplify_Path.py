class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        print(path)

        for el in path:
            if el == "..":
                if stack:
                    stack.pop()
            elif el and el != ".":
                stack.append(el)
            print(stack)

        return "/" + "/".join(stack)


path = "/../"
# Output: "/home/foo"

sol = Solution()

print(sol.simplifyPath(path))
