class Header(object):
    def __init__(self, offset, level):
        self._offset = offset
        self._level = level

    def advance_enumerator(self, e):
        e.add_enumerate(self._level)

    def offset(self):
        return self._offset

    def _tuple(self):
        return self._offset, self._level

    def __eq__(self, other):
        return other.__class__ == self.__class__ and self._tuple() == other._tuple()

    def __hash__(self):
        return hash(self._tuple())

    def __repr__(self):
        return "H(offset={}, level={})".format(self._offset, self._level)