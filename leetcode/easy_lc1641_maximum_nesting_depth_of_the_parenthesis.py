class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1 and (s != '(' or s != ')'):
            return 0
        else:
            max_depth = 0
            stack = []
            for i in range(0, len(s)):
                if s[i] == '(':
                    stack.append('(')
                if s[i] == ')':
                    stack.pop()
                max_depth = max(max_depth, len(stack))
        return max_depth


if __name__ == '__main__':
    #print(Solution().maxDepth("(1+(2*3)+((8)/4))+1D"))
    print(Solution().maxDepth("8*((1*(5+6))*(8/6))"))
