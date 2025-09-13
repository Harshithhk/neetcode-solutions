def dailyTemperatures(self, temperatures):
    res = []
    left = 0
    right = 1

    for i in range(len(temperatures) - 1):
        diff = temperatures[right] - temperatures[left]
        
        if diff > 0:
            res.append(diff)
        
        for j in range (len(temperatures) - i):
            diff = temperatures[right] - temperatures[left]
            