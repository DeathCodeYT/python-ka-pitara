


# Iterables: List,String,Tuples,Sets,Generators,Dictionaries

# my_list = [10,20,30]

# iterator = iter(my_list)
# iterator = my_list

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


class MyIterator:
    def __init__(self,maxV):
        self.max = maxV
    
    def __iter__(self):
        self._current = 0
        return self
    def __next__(self):
        if self._current < self.max:
            self._current += 1
            return self._current
        else:
            raise StopIteration

# it = MyIterator(10)

# myItr = iter(it)

# while True:
#     try:
#         print(next(myItr))
#     except StopIteration:
#         break


class EvenNumbers:
    def __init__(self,maxV):
        self.max = maxV
    
    def __iter__(self):
        self.num = 0
        return self
    def __next__(self):
        if self.num <= self.max:
            result = self.num
            self.num +=2
            return result
        else:
            raise StopIteration

even_nums = EvenNumbers(57)

for num in even_nums:
    print(num)


