class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([char.lower() for char in s if char.isalnum()])
        if len(s) != 0:
            for i in range(0, len(s)):
                if s[i] != s[-i-1]:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
