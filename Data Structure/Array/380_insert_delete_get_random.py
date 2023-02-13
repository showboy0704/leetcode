import random
class RandomizedSet:

    def __init__(self):
        self.table = dict()

    def insert(self, val: int) -> bool:
        if val not in self.table:
            self.table[val] = True
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.table:
            del self.table[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        keys = list(self.table.keys())
        random_int = random.randint(0,len(keys)-1)
        return keys[random_int]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
param_2 = obj.remove(1)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
