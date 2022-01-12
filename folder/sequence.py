
class UserSequence:
    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < self.number:
                return index
            else:
                raise IndexError

        if isinstance(index, slice):
            result = []
            start = index.start or 0
            stop = index.stop or -1
            step = index.step or 1
            if start >= 0 or stop < self.number:
                for elem in range(start, stop, step):
                    result.append(elem)
                return result
            else:
                raise IndexError
        else:
            raise TypeError()

    def __len__(self):
        return self.number
