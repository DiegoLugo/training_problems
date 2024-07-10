#1598. Crawler Log Folder
#https://leetcode.com/problems/crawler-log-folder/
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        for step in logs:
            if step == '../' and steps > 0:
                steps -= 1
            elif step[0] != '.':
                steps += 1
        return steps

if __name__ == '__main__':
    print(Solution().minOperations(["d1/","d2/","../","d21/","./"]))
    # print(Solution().minOperations(["d1/","d2/","./","d3/","../","d31/"]))