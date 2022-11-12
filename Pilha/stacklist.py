class ListStack(object):
    def _init_(self):
        self.stack = []
        self._size = 0

    def _len_(self):
        return self._size

    def clear(self):
        self.stack.clear()
        self._size = 0
        return self.stack

    def isEmpty(self):
        if self.stack:
            return False

    def _repr_(self):
        r = ""
        i = len(self.stack) - 1
        while i >= 0:
            r = r + str(self.stack[i]) + "\n"
            i -= 1
        return r

    def _str_(self):
        return self._repr_()

    def push(self, item):
        self.stack.append(item)
        self._size += 1

    def pop(self):
        if self.stack:
            self.stack.pop()
            self._size -= 1
        else:
            raise IndexError("The stack in empty")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("The stack in empty")