



class Deque:
## STUDENT TO RENAME TO class Deque ##
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self, data_list=None):
        if data_list is None:
            data_list = []
        if data_list is not None and not isinstance(data_list, list):
            data_list = [data_list]
        self.first = None
        self.last = None
        self.size = 0

        for data in data_list:
            self.enqueue(data)


    def enqueue(self, data):
        n = Deque.QueueNode(data)
        if self.first is None:  # EMPTY
            self.first = n
            self.last = n
        else:
            self.last.prev = n
            n.next = self.last
            self.last = n
        self.size += 1

    def dequeue(self):
        ret = self.first

        if self.size == 1:
            self.first = None
            self.last = None
        elif self.size > 1:
            self.first = self.first.prev
            self.first.next = None

        if self.size >= 1:
            self.size -= 1
            return ret.data
