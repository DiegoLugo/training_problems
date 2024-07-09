class Solution:
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        finish_time = 0
        sum_waiting = 0
        for customer in customers:
            #if finish_time == 0:
                #finish_time = customer[0]
            #if finish_time >= customer[0]:
                #finish_time += customer[1]
            #else:
                #finish_time = customer[0] + customer[1]
            finish_time = max(customer[0], finish_time) + customer[1]
            waiting_time = finish_time - customer[0]
            sum_waiting += waiting_time
        return (sum_waiting / len(customers))
    
if __name__ == '__main__':
    print(Solution().averageWaitingTime([[1,2],[2,5],[4,3]]))
    # print(Solution().averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))