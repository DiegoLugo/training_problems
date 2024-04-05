class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = len(s) - 1
        while i > 0:
            if ((s[i] != s[i - 1]) and (s[i] == s[i - 1].lower() or s[i] == s[i - 1].upper())):
                s = s[:i-1] + s[i+1:]
                i = len(s) - 1
            else:
                i -= 1
        return s


if __name__ == '__main__':
    print(Solution().makeGood("abBAcC"))
    #print(Solution().makeGood("leEeetcode"))
