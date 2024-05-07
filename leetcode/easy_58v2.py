# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        string.split() with no separator splits the string
        comboing any consecutive whitespaces and does
        strip under the hood (ignores whitespaces at the beginning and at the
        end of the string). If string is whitespaces only, returns []
        """
        return len(s.split()[-1])


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))
    # print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
