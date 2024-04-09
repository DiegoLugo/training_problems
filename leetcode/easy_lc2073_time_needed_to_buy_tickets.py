class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int

        On an interview ask if we wanna pop and append, because the problem can
        be solved without doing it like I did in this solution
        """
        time = 0
        curr = 0
        while True:
            if tickets[k] == 0:
                break
            else:
              curr = tickets.pop(0)
              if curr > 0:
                  curr -= 1
                  time += 1
                  tickets.append(curr)
              if k > 0:
                  k -= 1
              else:
                  k = len(tickets) - 1
        return time

if __name__ == '__main__':
    print(Solution().timeRequiredToBuy([2,3,2], 2))
    #print(Solution().timeRequiredToBuy([5,1,1,1], 0))
