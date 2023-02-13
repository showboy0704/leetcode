class NestedInteger:
    pass


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> NestedInteger:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: list[NestedInteger]):
        self.queue = []
        for nested in nestedList:
            stack = [nested]
            while stack:
                nest_int = stack.pop()
                if nest_int.isInteger():
                    self.queue.append(nest_int.getInteger())
                else:
                    stack.extend(nest_int.getList()[::-1])

    def next(self) -> int:
        nxt = self.queue[0]
        self.queue = self.queue[1:]
        return nxt

    def hasNext(self) -> bool:
        if self.queue:
            return True
        return False
