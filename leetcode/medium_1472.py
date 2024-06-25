# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/description/
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current = 0
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[0:self.current + 1]
        self.history.append(url)
        self.current = len(self.history) - 1
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        real_steps = 0
        if steps >= self.current:
            real_steps = self.current
        else:
            real_steps = steps
        for i in range(0, real_steps):
            self.current -= 1
        return self.history[self.current]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        real_steps = 0
        if steps >= ((len(self.history) - 1) - self.current):
            real_steps = (len(self.history) - 1) - self.current
        else:
            real_steps = steps
        for i in range(0, real_steps):
            self.current += 1
        return self.history[self.current]          


# Your BrowserHistory object will be instantiated and called as such:
#actions = ["BrowserHistory","visit","visit","back","visit","forward","visit","visit","forward","visit","back","visit","visit","forward"]
#params = [["esgriv.com"],["cgrt.com"],["tip.com"],[9],["kttzxgh.com"],[7],["crqje.com"],["iybch.com"],[5],["uun.com"],[10],["hci.com"],["whula.com"],[10]]
#actions = ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
#params = [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
#obj = BrowserHistory(params[0][0])
#for i in range(1, len(actions)):
#    if actions[i] == "visit":
#        obj.visit(params[i][0])
#    elif actions[i] == "back":
#        print(obj.back(params[i][0]))
#    elif actions[i] == "forward":
#        print(obj.forward(params[i][0]))
#    else:
#        print("Invalid action")

