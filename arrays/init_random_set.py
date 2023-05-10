class RandomizedSet:

    def __init__(self):
        self.hash = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        else:
            self.arr.append(val)
            self.hash[val] = len(self.arr) - 1
            return True


    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        else:
            idx = self.hash[val]
            self.hash[self.arr[-1]] = idx # reassign last value in arr
            self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1] # target to end of array
            self.arr.pop() #remove from end of array
            del self.hash[val] # remove target from hashmap
            return True

    def getRandom(self) -> int:
        return random.choice(self.arr)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
