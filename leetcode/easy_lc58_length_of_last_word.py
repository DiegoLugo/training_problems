class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        return len(s.split(' ').pop())


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))
    # print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
