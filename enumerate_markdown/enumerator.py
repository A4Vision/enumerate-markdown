
class Enumerator(object):
    def __init__(self):
        self._full_index = tuple()

    def _last_index(self):
        return self._full_index[-1]

    def _depth(self):
        return len(self._full_index)

    def add_enumerate(self, level):
        assert level > 0
        if level > self._depth() + 1:
            self.add_enumerate(level - 1)
        assert level <= self._depth() + 1
        if level == self._depth() + 1:
            self._full_index = self._full_index + (1,)
        elif level == self._depth():
            self._full_index = self._full_index[:-1] + (self._full_index[-1] + 1,)
        else:
            assert level < self._depth()
            self._full_index = self._full_index[:level]
            self.add_enumerate(level)

    def get_index(self):
        return self._full_index
