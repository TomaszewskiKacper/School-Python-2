class Zeroj:
    def __init__(self, lista):
        self.list = lista

    def another(self, siz, arr, res, result):   #recursive version
        if siz > 0: #if size not 0, append another element and go again
            for i, el in enumerate(arr):
                res.append(el)
                self.another(siz-1, arr[i+1:], res, result)
                res.pop()   #pop so elements don't repeat
        else:
            result.append(res.copy())   #size = 0, append to results
        
    def podlisty(self):
        result = []
        self.another(3, self.list, [], result)  #append every sublist to result

        return result

    def zerowe(self):
        result = []
        sublists = self.podlisty()  #every 3 element sublist
        for list in sublists:
            if sum(list) == 0:
                result.append(list)
        return result






lis = [1, 2, 3, 4, 5, 6, 7, -1, -2, -3, -4, -5 ,-6, -7]
l = Zeroj(lis)
print("Podlisty: ", l.zerowe())



