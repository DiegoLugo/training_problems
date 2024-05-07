# 1700. Number of Students Unable to Eat Lunch
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        i = 0
        while i < len(students):
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                i = 0
            else:
                students.append(students.pop(0))
                i += 1
        return len(students)


if __name__ == '__main__':
    print(Solution().countStudents([1, 1, 0, 0]))
    # print(Solution().countStudents([1,1,1,0,0,1]))
