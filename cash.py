import sys
class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, value):
         idx_of_slot = sys.getsizeof(value)
         return idx_of_slot

    def seek_slot(self, value):
        idx = 0
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                idx = (idx + self.hash_fun(self.slots[i]))
        idx = idx % self.size
        if idx == 0 and self.slots[idx] is None:
            return idx
        a = 0
        if idx > len(self.slots) - 1  or self.slots[idx] is not None:
            for i in range(1,len(self.slots)):
                a =  a + idx + (i * self.hash_fun(self.slots[i]))
                new_id = a % len(self.slots)
                if self.slots[new_id] is None:
                    return new_id
        if self.slots[idx] is None:
            return idx
        x = 0
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                x += 1
        if len(self.slots)  - x == 1:
            for i in range(len(self.slots)):
                if self.slots[i] is None:
                    return i
        return None
         # находит индекс пустого слота для значения, или None

    def put(self, value):
         # записываем значение по хэш-функции
        slot_num = self.seek_slot(value)
        if slot_num is not None:
            self.slots[slot_num] = value
            return slot_num
        else:
            min = 0
            idx = 0
            for i in range(len(self.hits)):
                if min < self.hits[i]:
                    min = self.hits[i]
                    idx = i
            self.slots[idx] = value
            return idx
         # возвращается индекс слота или None,
         # если из-за коллизий элемент не удаётся
         # разместить 

    def find(self, value):
        for i in range(len(self.slots)):
            if self.slots[i] == value:
                self.hits[i] +=1
                return i
        return None
