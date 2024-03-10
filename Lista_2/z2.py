class Podlist:
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
        result = [[]]
        for i in range(len(self.list)): #go over every possible size of sublist
            self.another(i+1, self.list, [], result)  #append every sublist to result

        return result




lis = [1,2,3]
l = Podlist(lis)
print("Podlisty: ", l.podlisty())



